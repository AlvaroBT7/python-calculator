from tkinter import *
from tkinter import ttk


class Calc:
    def __init__(self):
        self.number_a = 0
        self.number_b = 0
        self.buttons = {
            # "display": 
            "numeric_panel": [
                NumericCalcButton(text="0", command=lambda: self.add()),
                NumericCalcButton(text="1", command=lambda: self.add()),
                NumericCalcButton(text="2", command=lambda: self.add()),
                NumericCalcButton(text="3", command=lambda: self.add()),
                NumericCalcButton(text="4", command=lambda: self.add()),
                NumericCalcButton(text="5", command=lambda: self.add()),
                NumericCalcButton(text="6", command=lambda: self.add()),
                NumericCalcButton(text="7", command=lambda: self.add()),
                NumericCalcButton(text="8", command=lambda: self.add()),
            ]
        }
        self.__start = [
            self.grid_numeric_panel()
        ]

    
    def grid_numeric_panel(self):
        # for numeric_button in self.buttons["numeric_panel"]:
        #     numeric_button.pack()
        contador = 0
        for row in range(3):
            for column in range(3):
                self.buttons["numeric_panel"][contador].grid(row=row, column=column)
                contador += 1
        return self.buttons["numeric_panel"]


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

root.mainloop()