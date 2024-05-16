import pdfplumber
import json

def pdf_to_json(pdf_path, json_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            data = []
            for page in pdf.pages:
                page_data = {
                    "page_number": page.page_number,
                    "text": page.extract_text(),
                    "images": []
                }

                for img in page.images:
                    img_data = {
                        "width": img["width"],
                        "height": img["height"],
                        "data": img["data"]
                    }
                    page_data["images"].append(img_data)

                data.append(page_data)
        
        with open(json_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except Exception as e:
        print("Conversion Failed:", e)

# Örnek kullanım:
# pdf_to_json("sample2.pdf", "PdfToJson.json")
