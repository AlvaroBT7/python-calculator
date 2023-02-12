from tkinter import *
from tkinter import ttk

class CalcButton(ttk.Button):
    def __init__(self, **kwargs):
        super().__init__(
            root,
            text=kwargs["text"],
            command=kwargs["command"]
            )

root = Tk()
root.geometry("400x400")
root.resizable(False, False)

CalcButton(text="hola", command = lambda: print("Hola pedro")).pack()

root.mainloop()