import json
import pdfplumber


def pdf_to_json(pdf_path):
    data = {}
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_data = {}
            page_data['text'] = page.extract_text()
            # Buraya diğer veri türlerini de ekleyebilirsiniz (görüntüler, tablolar, vs.)
            data[f'page_{i+1}'] = page_data
    with open(f"{pdf_path[:-4]}.json", 'w') as json_file:
        json.dump(data, json_file)