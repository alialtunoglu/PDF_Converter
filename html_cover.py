from spire.pdf.common import *
from spire.pdf import *

def pdf_to_html(pdf_path, html_path):
    doc = PdfDocument()
    try:
        doc.LoadFromFile(pdf_path)
        doc.SaveToFile(html_path, FileFormat.HTML)
    except Exception as e:
        print("Conversion Failed:", e)
    finally:
        doc.Close()

# Örnek kullanım:
# pdf_to_html("sample2.pdf", "PdfToHtml.html")
