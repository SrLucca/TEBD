from db import close_database

def sair(root):
    root.destroy()
    close_database()
