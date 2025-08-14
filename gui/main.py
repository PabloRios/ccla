import glob
import os
import tkinter as tk
import strings
from tkinter import ttk, messagebox
import processPath
import processText


class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(strings.APP_TITLE)
        self.root.geometry("600x480")

        self.label_path = ttk.Label(self.root, text=strings.PDF_PATH_LABEL)
        self.label_path.pack(pady=5)

        self.entry_path = ttk.Entry(self.root, width=40)
        self.entry_path.pack(pady=5)

        self.btn_procesar = ttk.Button(
            self.root, text=strings.PROCESS_BUTTON, command=self.procesar_pdf)
        self.btn_procesar.pack(pady=10)

        self.text_output = tk.Text(self.root, wrap="word", height=6)
        self.text_output.pack(fill="both", expand=True, padx=10, pady=5)

    def procesar_pdf(self):
        path = self.entry_path.get().strip()
        if not path:
            messagebox.showerror(
                strings.ERROR, strings.ERROR_NO_PATH)
            return

        try:

            texts = processPath.processPath(args.path)
            facturas = processText.processText(texts)

            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, facturas)

        except Exception as e:
            messagebox.showerror(
                strings.ERROR, f"{strings.ERROR_READ_PDF}:\n{e}")

    def run(self):
        self.root.mainloop()
