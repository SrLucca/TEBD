import tkinter as tk
from game import jogar
from how_to_play import como_jogar


def sair():
    root.destroy()


root = tk.Tk()
root.title("Sabonete")


window_width = 800
window_height = 600


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)


root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")


frame = tk.Frame(root)
frame.pack(expand=True)


btn_jogar = tk.Button(frame, text="Jogar", command=jogar)
btn_como_jogar = tk.Button(frame, text="Como Jogar", command=como_jogar)
btn_sair = tk.Button(frame, text="Sair", command=sair)


btn_jogar.pack(pady=10)
btn_como_jogar.pack(pady=10)
btn_sair.pack(pady=10)


root.mainloop()
