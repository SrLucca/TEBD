import tkinter as tk
from game import jogar
from how_to_play import como_jogar
from handler.exit import sair

root = tk.Tk()
root.title("Sabonete")


def inicia_jogo():
    jogar(root)


def fecha_menu():
    sair(root)


window_width = 800
window_height = 600


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)


root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")


frame = tk.Frame(root)
frame.pack(expand=True)


btn_jogar = tk.Button(frame, text="Jogar", command=inicia_jogo)
btn_como_jogar = tk.Button(frame, text="Como Jogar", command=como_jogar)
btn_sair = tk.Button(frame, text="Sair", command=fecha_menu)

btn_jogar.pack(pady=10)
btn_como_jogar.pack(pady=10)
btn_sair.pack(pady=10)


root.mainloop()
