import subprocess
import tabula



def pdf_to_html(pdf_path):
    # PDF'den veriyi çıkar
    tables = tabula.read_pdf_with_template(pdf_path, pages="all")

    # Çıkarılan veriyi HTML tablolarına dönüştürme
    html_tables = []
    for table in tables:
        html_table = table.to_html()
        html_tables.append(html_table)

    # HTML tablolarını bir dosyaya yazma
    with open(f"{pdf_path[:-4]}.html", "w", encoding="utf-8") as f:
        for html_table in html_tables:
            f.write(html_table)

    # pdf2htmlEX komutunu kullanarak PDF'yi HTML'ye dönüştür
    #subprocess.run(["pdf2htmlEX", pdf_path, f"{pdf_path[:-4]}.html"])

