from tkinter import messagebox
import tkinter as tk
import time
from handler.exit import sair


def jogar(root):

    for widget in root.winfo_children():
        widget.destroy()

    # Desenha a nova tela do jogo
    lbl_jogo = tk.Label(root, text="Tela do Jogo", font=("Helvetica", 16))
    lbl_jogo.pack(pady=20)

    btn_sair = tk.Button(root, text="Sair", command=lambda: sair(root))
    btn_sair.pack(pady=10)
