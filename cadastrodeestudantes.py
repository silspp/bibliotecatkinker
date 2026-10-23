import tkinter as tk
from tkinter import messagebox
import re

estudantes = []

def cadastrar():
    nome = entrada_nome.get().strip()
    matricula = entrada_matricula.get().strip()
    email = entrada_email.get().strip()

    if not nome or not matricula or not email:
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos!"
        )
        return

    if not re.fullmatch(r"\d{6}", matricula):
        messagebox.showerror(
            "Erro",
            "A matrícula deve ter 6 dígitos."
        )
        return

    if not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", email
    ):
        messagebox.showerror(
            "Erro",
            "Digite um e-mail em formato válido."
        )
        return

    estudante = {
        "nome": nome,
        "matricula": matricula,
        "email": email
    }

    estudantes.append(estudante)

    lista.insert(
        tk.END,
        f"{nome} | {matricula} | {email}"
    )

    entrada_nome.delete(0, tk.END)
    entrada_matricula.delete(0, tk.END)
    entrada_email.delete(0, tk.END)

    messagebox.showinfo(
        "Sucesso",
        "Estudante cadastrado!"
    )

janela = tk.Tk()
janela.title("Cadastro de Estudantes")
janela.geometry("520x480")

tk.Label(
    janela,
    text="Cadastro de Estudantes",
    font=("Arial", 16, "bold")
).pack(pady=10)

tk.Label(janela, text="Nome:").pack()
entrada_nome = tk.Entry(janela, width=45)
entrada_nome.pack(pady=4)

tk.Label(janela, text="Matrícula (6 dígitos):").pack()
entrada_matricula = tk.Entry(janela, width=45)
entrada_matricula.pack(pady=4)

tk.Label(janela, text="E-mail:").pack()
entrada_email = tk.Entry(janela, width=45)
entrada_email.pack(pady=4)

tk.Button(
    janela,
    text="Cadastrar estudante",
    command=cadastrar
).pack(pady=12)

tk.Label(
    janela,
    text="Estudantes cadastrados:",
    font=("Arial", 11, "bold")
).pack()

lista = tk.Listbox(janela, width=65, height=9)
lista.pack(pady=8)

janela.mainloop()
