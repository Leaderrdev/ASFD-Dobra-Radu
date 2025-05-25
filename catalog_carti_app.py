import tkinter as tk
from tkinter import messagebox
import json
import os

FISIER_JSON = "carti.json"

class CatalogCartiApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Catalog de Cărți")
        self.master.geometry("500x300")

        self.carti = self.incarca_date()

        self.lista = tk.Listbox(master, width=50)
        self.lista.pack(pady=10)

        self.btn_frame = tk.Frame(master)
        self.btn_frame.pack()
        tk.Button(self.btn_frame, text="Adaugă", command=self.adauga).pack(side="left", padx=5)
        tk.Button(self.btn_frame, text="Editează", command=self.editeaza).pack(side="left", padx=5)
        tk.Button(self.btn_frame, text="Șterge", command=self.sterge).pack(side="left", padx=5)

        self.afiseaza_lista()

    def afiseaza_lista(self):
        self.lista.delete(0, tk.END)
        for carte in self.carti:
            self.lista.insert(tk.END, f"{carte['titlu']} - {carte['autor']}")

    def incarca_date(self):
        if os.path.exists(FISIER_JSON):
            with open(FISIER_JSON, "r") as f:
                return json.load(f)
        return []

    def salveaza_date(self):
        with open(FISIER_JSON, "w") as f:
            json.dump(self.carti, f, indent=4)

    def adauga(self):
        self.formular()

    def editeaza(self):
        selectie = self.lista.curselection()
        if not selectie:
            messagebox.showwarning("Atenție", "Selectează o carte pentru editare.")
            return
        index = selectie[0]
        self.formular(index)

    def sterge(self):
        selectie = self.lista.curselection()
        if not selectie:
            messagebox.showwarning("Atenție", "Selectează o carte pentru ștergere.")
            return
        index = selectie[0]
        confirmare = messagebox.askyesno("Confirmare", "Ești sigur că vrei să ștergi această carte?")
        if confirmare:
            del self.carti[index]
            self.salveaza_date()
            self.afiseaza_lista()

    def formular(self, index=None):
        fereastra = tk.Toplevel(self.master)
        fereastra.title("Formular carte")

        tk.Label(fereastra, text="Titlu:").pack()
        entry_titlu = tk.Entry(fereastra)
        entry_titlu.pack()

        tk.Label(fereastra, text="Autor:").pack()
        entry_autor = tk.Entry(fereastra)
        entry_autor.pack()

        if index is not None:
            carte = self.carti[index]
            entry_titlu.insert(0, carte["titlu"])
            entry_autor.insert(0, carte["autor"])

        def salveaza():
            titlu = entry_titlu.get()
            autor = entry_autor.get()
            if not titlu or not autor:
                messagebox.showerror("Eroare", "Completează toate câmpurile.")
                return
            carte = {"titlu": titlu, "autor": autor}
            if index is None:
                self.carti.append(carte)
            else:
                self.carti[index] = carte
            self.salveaza_date()
            self.afiseaza_lista()
            fereastra.destroy()

        tk.Button(fereastra, text="Salvează", command=salveaza).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogCartiApp(root)
    root.mainloop()
