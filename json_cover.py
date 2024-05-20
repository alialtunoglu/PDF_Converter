import fitz  # PyMuPDF
import json
import os
import pdfplumber


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        for page in pdf.pages:
            page_data = {
                "page_number": page.page_number,
                "width": page.width,
                "height": page.height,
                "words": []
            }
            for word in page.extract_words():
                page_data["words"].append({
                    "text": word["text"],
                    "x0": word["x0"],
                    "top": page.height - word["top"],  # Y koordinatını ters çevir
                    "width": word["width"],
                    "height": word["height"]
                })
            raw_text = page.extract_text()
            page_data["raw_text"] = raw_text.strip()
            pages.append(page_data)

        # Tüm sayfaların metinlerini birleştirerek bir paragraf oluştur
        all_text = " ".join([page["raw_text"] for page in pages])
        # Son sayfada oluşturulan metni output.json dosyasına ekleyelim
        pages[-1]["raw_text"] = all_text

        return pages


def pdf_to_json(pdf_path, json_path):
    text_data = extract_text_from_pdf(pdf_path)
    doc = fitz.open(pdf_path)
    data = {"pages": []}

    # Determine output directory
    output_dir = os.path.dirname(json_path)
    image_dir = os.path.join(output_dir, "_images")

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    for page_number, page_text in enumerate(text_data):
        page = doc.load_page(page_number)
        text = page.get_text()
        images = page.get_images(full=True)

        page_data = {"words": page_text["words"], "images": []}

        for img_index, img_info in enumerate(images):
            xref = img_info[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image_name = f"{os.path.basename(pdf_path)}_page_{page_number}_image_{img_index}.png"
            image_path = os.path.join(image_dir, image_name)
            image_url = f"file://{image_path}"

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            page_data["images"].append({"index": img_index, "url": image_url})

        data["pages"].append(page_data)

        # Add raw text to page data
        page_data["raw_text"] = text.strip()

    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"JSON dosyası oluşturuldu: {json_path}")

# Örnek kullanım:
# pdf_to_json("sample2.pdf", "output.json")
