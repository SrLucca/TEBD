import tkinter as tk
from handler.exit import sair
from tkinter import messagebox
import random

class DragDropApp:

    def __init__(self, button, root):
        self.root = root
        self.button = button
        self.button.bind("<Button-1>", self.on_start)
        self.button.bind("<B1-Motion>", self.on_drag)
        self.button.bind("<ButtonRelease-1>", self.on_drop)
        self._drag_data = {"x": 0, "y": 0}

    def on_start(self, event):
        """Called on button press to start dragging."""
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
        self.button.lift()

    def on_drag(self, event):
        """Called on mouse movement to drag the widget."""
        x = self.button.winfo_x() + event.x - self._drag_data["x"]
        y = self.button.winfo_y() + event.y - self._drag_data["y"]
        self.button.place(x=x, y=y)

    def on_drop(self, event):
        """Called on button release to end dragging."""
        pass

TURNO = 1  # Inicializa a variável TURNO

def test_func(btn_carta, carta, turno_label):
    global TURNO  # Referenciando a variável global
    btn_carta.config(text=carta)
    
    # Trocar turno
    if TURNO == 1:
        TURNO = 0
    else:
        TURNO = 1

    # Atualizar o label de turno
    turno_label.config(text=f"Turno: {TURNO}")

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
        "A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "J", "Q", "K", "A", "2", "3", "4", "5", "6", "7"
    ]
    random.shuffle(cartas)

    turno_label = tk.Label(root, text=f"Turno: {TURNO}")
    turno_label.pack()

    # Função para criar botões de cartas
    def criar_botao_carta(root, carta, x, y):
        btn_carta = tk.Button(root, text="?", width=10, height=5, command=lambda: test_func(btn_carta, carta, turno_label))
        DragDropApp(btn_carta, root)  # Inicializa o DragDropApp para este botão
        btn_carta.place(x=x, y=y)
        return btn_carta

    # Adiciona 20 botões de cartas em posições aleatórias
    for i in range(20):
        carta_escolhida = cartas.pop()
        x = random.randint(50, 500)  # Ajuste os valores conforme necessário
        y = random.randint(50, 300)  # Ajuste os valores conforme necessário
        criar_botao_carta(root, carta_escolhida, x, y)

    btn_monte = tk.Button(root, text="Monte", command=lambda: print("Monte clicado"))
    btn_monte.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  

    btn_sair = tk.Button(root, text="Sair", command=lambda: sair(root))
    btn_sair.pack(pady=10)