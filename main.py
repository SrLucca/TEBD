import tkinter as tk
from game import iniciar_jogo
from how_to_play import como_jogar
from handler.exit import sair
from playsound import playsound
from multiprocessing import Process


root = tk.Tk()
root.title("Jogo da Bruxa")


def inicia_jogo():
    iniciar_jogo(root)


def fecha_menu():
    sair(root)



window_width = 1280
window_height = 720


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

