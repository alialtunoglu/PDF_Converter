import pdfplumber

def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    with open(f"{pdf_path[:-4]}.txt", 'w', encoding='utf-8') as file:
        file.write(text)

    return text



