
import tkinter as tk
from tkinter import messagebox

def executar():
    dado = campo.get().strip()

    if dado == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha o campo!"
        )
        return

    resultado.config(
        text=f"Você informou: {dado}"
    )

janela = tk.Tk()
janela.title("Projeto Python")
janela.geometry("400x300")

titulo = tk.Label(
    janela,
    text="Sistema do Grupo",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=15)

campo = tk.Entry(janela, width=30)
campo.pack(pady=10)

botao = tk.Button(
    janela,
    text="Executar",
    command=executar
)
botao.pack(pady=10)

resultado = tk.Label(
    janela,
    text="O resultado aparecerá aqui."
)
resultado.pack(pady=10)

janela.mainloop()
