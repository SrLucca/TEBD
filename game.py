import tkinter as tk
from handler.exit import sair
from tkinter import messagebox

def test_func(carta):
    messagebox.showinfo(f"Carta: {carta}")

def jogar(root):
    for widget in root.winfo_children():
        widget.destroy()

    # Desenha a nova tela do jogo
    lbl_jogo = tk.Label(root, text="Tela do Jogo", font=("Helvetica", 16))
    lbl_jogo.pack(pady=20)

    frame_superior = tk.Frame(root)
    frame_superior.pack()

    frame_inferior = tk.Frame(root)
    frame_inferior.pack()

    
    cartas = [
        "A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠",
        "J♠", "Q♠", "K♠", "A♥", "2♥", "3♥", "4♥", "5♥", "6♥", "7♥"
    ]

    # Adiciona 10 botões na metade superior
    for i in range(10):
        btn_carta = tk.Button(frame_superior, text=cartas[i], width=10, height=5, command=lambda c=cartas[i]: test_func(c))
        btn_carta.grid(row=i//10, column=i%10, padx=10, pady=10)

    # Adiciona 10 botões na metade inferior
    for i in range(10, 20):
        btn_carta = tk.Button(frame_inferior, text=cartas[i], width=10, height=5, command=lambda c=cartas[i]: test_func(c))
        btn_carta.grid(row=(i-10)//10, column=(i-10)%10, padx=10, pady=150)
    
    btn_monte = tk.Button(root, text="Monte", command=lambda: print("Monte clicado"))
    btn_monte.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  

    btn_sair = tk.Button(root, text="Sair", command=lambda: sair(root))
    btn_sair.pack(pady=10)

