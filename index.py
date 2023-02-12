from tkinter import *
from tkinter import ttk


class Calc:
    def __init__(self):
        self.number_a = 0
        self.number_b = 0
        self.buttons = {
            "display": CalcDisplay(text="display calculator"),
            "numeric_panel": [
                NumericCalcButton(text="0", command=lambda: self.print_in_display("0")),
                NumericCalcButton(text="1", command=lambda: self.print_in_display("1")),
                NumericCalcButton(text="2", command=lambda: self.print_in_display("2")),
                NumericCalcButton(text="3", command=lambda: self.print_in_display("3")),
                NumericCalcButton(text="4", command=lambda: self.print_in_display("4")),
                NumericCalcButton(text="5", command=lambda: self.print_in_display("5")),
                NumericCalcButton(text="6", command=lambda: self.print_in_display("6")),
                NumericCalcButton(text="7", command=lambda: self.print_in_display("7")),
                NumericCalcButton(text="8", command=lambda: self.print_in_display("8")),
            ]
        }
        self.__start = [
            self.grid_calc_buttons()
        ]

    
    def grid_calc_buttons(self):

        # grids calculator display
        self.buttons["display"].grid(row=0, column=1)

        # grids the numeric button panel
        conter = 0
        for row in range(3):
            for column in range(3):
                self.buttons["numeric_panel"][conter].grid(row=row+1, column=column)
                conter += 1
        return self.buttons["numeric_panel"]


    def print_in_display(self, pressed_button):
        new_display_content = self.buttons["display"].cget("text")
        new_display_content += pressed_button
        self.buttons["display"].config(text=new_display_content)


class CalcDisplay(ttk.Label):
    def __init__(self, **kwargs):
        super().__init__(
            root,
            text=kwargs["text"],
            background="#222222",
            foreground="#ffffff",
            font=("Cascadia Code", 20, "bold")
        )


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
root.resizable(False, False)

calc1 = Calc()

root.mainloop()