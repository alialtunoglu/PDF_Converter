import html_cover
import text_cover
import word_cover
import json_cover

import tkinter as tk
from tkinter import filedialog, messagebox

def select_pdf_file():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path_entry.delete(0, tk.END)
    pdf_path_entry.insert(0, pdf_path)


def convert_to_word():
    pdf_path = pdf_path_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    if output_path:
        word_cover.pdf_to_word(pdf_path, output_path)
        messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")

def convert_to_html():
    pdf_path = pdf_path_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if output_path:
        html_cover.pdf_to_html(pdf_path, output_path)
        messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")



def convert_to_json():
    pdf_path = pdf_path_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if output_path:
        json_cover.pdf_to_json(pdf_path, output_path)
        messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")



def convert_to_txt():
    text_cover.pdf_to_text(pdf_path_entry.get())
    messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")

def convert():
    convert_to_word()
    convert_to_json()
    convert_to_html()
    convert_to_txt()

root = tk.Tk()
root.title("PDF Converter")

pdf_path_label = tk.Label(root, text="Select PDF File:")
pdf_path_label.grid(row=0, column=0, padx=10, pady=5)

pdf_path_entry = tk.Entry(root, width=50)
pdf_path_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

browse_button = tk.Button(root, text="Browse", command=select_pdf_file)
browse_button.grid(row=0, column=3, padx=10, pady=5)

word_button = tk.Button(root, text="Convert to Word", command=convert_to_word)
word_button.grid(row=1, column=0, padx=10, pady=5)

json_button = tk.Button(root, text="Convert to JSON", command=convert_to_json)
json_button.grid(row=1, column=1, padx=10, pady=5)

html_button = tk.Button(root, text="Convert to HTML", command=convert_to_html)
html_button.grid(row=1, column=2, padx=10, pady=5)

txt_button = tk.Button(root, text="Convert to TXT", command=convert_to_txt)
txt_button.grid(row=1, column=3, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert All", command=convert)
convert_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

