import html_cover
import text_cover
import word_cover
import json_cover

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def select_pdf_file():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path_entry.delete(0, tk.END)
    pdf_path_entry.insert(0, pdf_path)


def select_output_directory():
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)


def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.title("Converting...")
    loading_screen.geometry("300x100")

    progress = ttk.Progressbar(loading_screen, orient="horizontal", length=200, mode="determinate")
    progress.pack(pady=20)

    tk.Label(loading_screen, text="Please wait...").pack()

    return loading_screen, progress


def update_progress(progress, current, total, loading_screen, callback, *args):
    progress["value"] = (current / total) * 100
    if current < total:
        root.after(50, update_progress, progress, current + 1, total, loading_screen, callback, *args)
    else:
        loading_screen.destroy()
        callback(*args)
        messagebox.showinfo("Başarılı", "PDF dönüştürme işlemi tamamlandı.")


def convert_file(converter, pdf_path, output_dir, extension):
    if output_dir:
        base_name = os.path.basename(pdf_path)
        output_file = os.path.join(output_dir, f"{os.path.splitext(base_name)[0]}.{extension}")
    else:
        output_file = filedialog.asksaveasfilename(defaultextension=f".{extension}",
                                                   filetypes=[(f"{extension.upper()} files", f"*.{extension}")])

    if output_file:
        loading_screen, progress = show_loading_screen()
        root.after(50, update_progress, progress, 0, 100, loading_screen, converter, pdf_path, output_file)


def convert_to_word():
    convert_file(word_cover.pdf_to_word, pdf_path_entry.get(), output_dir_entry.get(), "docx")


def convert_to_html():
    convert_file(html_cover.pdf_to_html, pdf_path_entry.get(), output_dir_entry.get(), "html")


def convert_to_json():
    convert_file(json_cover.pdf_to_json, pdf_path_entry.get(), output_dir_entry.get(), "json")


def convert_to_txt():
    convert_file(text_cover.pdf_to_text, pdf_path_entry.get(), output_dir_entry.get(), "txt")


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

output_dir_label = tk.Label(root, text="Select Output Directory:")
output_dir_label.grid(row=1, column=0, padx=10, pady=5)

output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

output_dir_button = tk.Button(root, text="Browse", command=select_output_directory)
output_dir_button.grid(row=1, column=3, padx=10, pady=5)

word_button = tk.Button(root, text="Convert to Word", command=convert_to_word)
word_button.grid(row=2, column=0, padx=10, pady=5)

json_button = tk.Button(root, text="Convert to JSON", command=convert_to_json)
json_button.grid(row=2, column=1, padx=10, pady=5)

html_button = tk.Button(root, text="Convert to HTML", command=convert_to_html)
html_button.grid(row=2, column=2, padx=10, pady=5)

txt_button = tk.Button(root, text="Convert to TXT", command=convert_to_txt)
txt_button.grid(row=2, column=3, padx=10, pady=5)

convert_button = tk.Button(root, text="Convert All", command=convert)
convert_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
