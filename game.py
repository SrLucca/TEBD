import tkinter as tk
from handler.exit import sair
from tkinter import messagebox
import random
from PIL import ImageTk, Image

class DragDropApp:

    def __init__(self, button, root, game):
        self.root = root
        self.button = button
        self.game = game
        self.button.bind("<Button-1>", self.on_start)
        self.button.bind("<B1-Motion>", self.on_drag)
        self.button.bind("<ButtonRelease-1>", self.on_drop)
        self._drag_data = {"x": 0, "y": 0}
        self.photos = []

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
        self.game.check_winner(self.button.winfo_y())

TURNO = 1  # Inicializa a variável TURNO

def test_func(btn_carta, carta):
    btn_carta.config(text=carta)
    
    

def change_turno(turno_label):
    global TURNO  # Referenciando a variável global
    if TURNO == 1:
        TURNO = 0
    else:
        TURNO = 1

    turno_label.config(text=f"Vez do jogador {TURNO}!")
    

class Game:
    def __init__(self, root):
        self.root = root
        self.cartas = [
            "10_copas", "2_ouros", "3_paus", "5_copas", "6_espadas", "7_ouros", "8_paus", "A_espadas", "joker", "Q_copas",
            "10_espadas", "2_paus", "4_copas", "5_espadas", "6_ouros", "7_paus", "9_copas", "A_ouros", "J_ouros", "Q_espadas",
            "10_ouros", "3_copas", "4_espadas", "5_ouros", "6_paus", "8_copas", "9_espadas", "A_paus", "K_copas", "Q_ouros",
            "2_copas", "3_espadas", "4_ouros", "5_paus", "7_copas", "8_espadas", "9_ouros", "J_copas", "K_espadas", "Q_paus",
            "2_espadas", "3_ouros", "4_paus", "6_copas", "7_espadas", "8_ouros", "A_copas", "J_espadas", "K_ouros"
            ]
        random.shuffle(self.cartas)
        self.turno_label = None
        self.jogar()

    def jogar(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root = self.root
        
        # Desenha a nova tela do jogo
        lbl_jogo = tk.Label(self.root, text="Tela do Jogo", font=("Helvetica", 16))
        lbl_jogo.pack(pady=20)

        frame_superior = tk.Frame(self.root)
        frame_superior.pack()

        frame_inferior = tk.Frame(self.root)
        frame_inferior.pack()

        self.turno_label = tk.Label(self.root, text=f"Vez do jogador {TURNO}!")
        self.turno_label.pack()

        # Função para criar botões de cartas
        def criar_botao_carta(root, carta, x, y, foto):
            btn_carta = tk.Button(root, text="?", width=50, height=130, image=foto, compound=tk.TOP, command=lambda: test_func(btn_carta, carta))
            instancia = DragDropApp(btn_carta, root, self)  # Inicializa o DragDropApp para este botão
            instancia.photos.append(foto)
            btn_carta.place(x=x, y=y)
            btn_carta.bind("<Button-3>", lambda event: btn_carta.destroy())  # Bind para excluir o botão com o botão direito
            return btn_carta

        def criar_nova_carta():
            carta = self.cartas[random.randint(0, len(self.cartas)-1)]
            self.cartas.remove(carta)
            photo = ImageTk.PhotoImage(Image.open(f'assets/{carta}.jpeg').resize((80,100)))
            criar_botao_carta(root=self.root, carta=carta, x=-10, y=-10, foto=photo)

        # Adiciona 20 botões de cartas em posições aleatórias
        espaco1 = 0
        espaco2 = 0
        for i in range(20):
            x = 0
            y = 0
            carta_escolhida = self.cartas[random.randint(0, len(self.cartas)-1)]
            self.cartas.remove(carta_escolhida)
            photo = ImageTk.PhotoImage(Image.open(f'assets/{carta_escolhida}.jpeg').resize((80,100)))
            if i > 9:
                x = 70 + espaco1
                y = 150
                espaco1 += 120
            else:
                x = 70 + espaco2
                y = 500
                espaco2 += 120
            criar_botao_carta(root=self.root, carta=carta_escolhida, x=x, y=y, foto=photo)

        btn_monte = tk.Button(self.root, text="Monte", command=criar_nova_carta)
        btn_monte.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  

        btn_sair = tk.Button(self.root, text="Sair", command=lambda: sair(self.root))
        btn_sair.pack(pady=10)

        btn_turno = tk.Button(self.root, text="Passar a vez", command=lambda: change_turno(self.turno_label))
        btn_turno.pack(pady=250)
        print(self.cartas)
    def check_winner(self, y):
        def get_cartas_em_ordem(y_position):
            cartas = []
            cartas_superior = []
            cartas_inferior = []
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button) and (widget.winfo_y() == y_position >= 50) and (widget.winfo_y() == y_position <= 250):
                    carta_text = widget.cget("text")
                    print(carta_text)
                    if carta_text.isdigit():
                        cartas_superior.append(int(carta_text))
                    elif carta_text == "A":
                        cartas_superior.append(1)
                    elif carta_text == "J":
                        cartas_superior.append(11)
                    elif carta_text == "Q":
                        cartas_superior.append(12)
                    elif carta_text == "K":
                        cartas_superior.append(13)
                    
                if isinstance(widget, tk.Button) and (widget.winfo_y() == y_position >= 450) and (widget.winfo_y() == y_position <= 650):
                    carta_text = widget.cget("text")
                    cartas_inferior.append(carta_text)
                    if carta_text.isdigit():
                        cartas_inferior.append(int(carta_text))
                    elif carta_text == "A":
                        cartas_inferior.append(1)
                    elif carta_text == "J":
                        cartas_inferior.append(11)
                    elif carta_text == "Q":
                        cartas_inferior.append(12)
                    elif carta_text == "K":
                        cartas_inferior.append(13)

            print(f'superior: {cartas_superior}')
            print(f'inferior: {cartas_inferior}')

            if cartas_superior == list(range(1, 11)):
                messagebox.showinfo("Vencedor", "Jogador Superior venceu!")
                self.jogar()
            elif cartas_inferior == list(range(1, 11)):
                messagebox.showinfo("Vencedor", "Jogador Inferior venceu!")
                self.jogar()

        get_cartas_em_ordem(y)

        

def iniciar_jogo(root):
    Game(root)

