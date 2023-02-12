from tkinter import *
from tkinter import ttk


class Calc:
    def __init__(self):
        self.number_a = 0
        self.number_b = 0
        self.buttons = {
            "numeric_panel": [
                NumericCalcButton(text="0", command=lambda: self.add())
            ]
        }
    
    def add(self):
        self.number_a += 1
        return print(self.number_a)


class CalcButton(ttk.Button):
    def __init__(self, **kwargs):
        super().__init__(
            root,
            text=kwargs["text"],
            command=kwargs["command"]
        )
        
class NumericCalcButton(CalcButton):
    def __init__(self, **kwargs):
        super().__init__(
            text=kwargs["text"],
            command=kwargs["command"]
        )


root = Tk()
# widget settings
root.geometry("400x400")
root.resizable(False, False)

calc1 = Calc()
calc1.buttons["numeric_button_1"].pack()

root.mainloop()