import fitz  # PyMuPDF kütüphanesi


def pdf_to_text(pdf_path, output_path):
    try:
        # PDF dosyasını aç
        document = fitz.open(pdf_path)
        text = ""

        # Her sayfayı oku ve metni biriktir
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        # Metni belirtilen dosyaya kaydet
        with open(output_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        print("PDF başarıyla metin dosyasına dönüştürüldü.")
    except Exception as e:
        print(f"Dönüştürme sırasında bir hata oluştu: {e}")
