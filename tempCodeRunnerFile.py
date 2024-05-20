from tkinter import messagebox

import text_cover
from main import pdf_path_entry


def convert_to_txt():
    text_cover.pdf_to_text(pdf_path_entry.get())
    messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")