import pdfplumber
from docx import Document

def pdf_to_word(pdf_path):
    doc = Document()

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            doc.add_paragraph(text)
    doc.save(f"{pdf_path[:-4]}.doc")
