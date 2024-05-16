from pdf2docx import Converter

def pdf_to_word(pdf_path, output_path):
    try:
        cv_obj = Converter(pdf_path)
        cv_obj.convert(output_path)
        cv_obj.close()
    except Exception as e:
        print("Conversion Failed:", e)
    else:
        print("File converted successfully")

# Örnek kullanım:
# pdf_to_word('sample2.pdf', 'output.docx')
