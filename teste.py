import tkinter as tk
def apenas_numeros(event):
    if event.char.isnumeric() is False:
        return "break"

root = tk.Tk()
entrada = tk.Entry(root)
entrada.pack()
entrada.bind("<Key>", apenas_numeros)
root.mainloop()