
def convert_to_txt():
    text_cover.pdf_to_text(pdf_path_entry.get())
    messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")