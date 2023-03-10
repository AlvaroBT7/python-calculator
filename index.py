from tkinter import *
from tkinter import ttk


class Calc:
    def __init__(self, parent):
        self.__parent = parent
        self.__number_a = 0
        self.__number_b = 0
        self.__display = CalcDisplay(self.__parent, text="display calculator")
        self.__buttons = {
            "numeric_panel": [NumericCalcButton(self.__parent, text=str(z), command=lambda: self.print_in_display(str(z))) for z in range(9)],
            "working_buttons": [
                WorkingCalcButton(self.__parent, text="Undo", command=lambda: self.clear_display()),
                WorkingCalcButton(self.__parent, text="Remove", command=lambda: self.remove_display_char()),
                WorkingCalcButton(self.__parent, text="=", command=lambda: print(f"has hecho click en {self.__buttons['working_buttons'][2].cget('text')}"))
            ]
        }
        self.grid_calc_buttons()

    
    def grid_calc_buttons(self):

        # grids calculator display
        display_grid_row = 0
        self.__display.grid(row=display_grid_row, column=1)

        # grids the numeric button panel
        conter = 0
        for row in range(3):
            for column in range(3):
                self.__buttons["numeric_panel"][conter].grid(row=row+display_grid_row+1, column=column)
                conter += 1
        
        # grids working buttons
        last_element_row = self.__buttons["numeric_panel"][-1].grid_info()["row"]
        self.__buttons["working_buttons"][0].grid(row=last_element_row+1, column=0)
        self.__buttons["working_buttons"][1].grid(row=last_element_row+1, column=1)
        self.__buttons["working_buttons"][2].grid(row=last_element_row+1, column=2)
        
        return self.__buttons


    def print_in_display(self, pressed_button):
        new_display_content = self.__display.cget("text")
        new_display_content += pressed_button
        self.__display.config(text=new_display_content)
        print(pressed_button)
        return pressed_button


    def remove_display_char(self):
        current_display_content = self.__display.cget("text")
        return self.__display.config(text=current_display_content[:-1])

    
    def clear_display(self):
        return self.__display.config(text="")


class CalcDisplay(ttk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text=kwargs["text"],
            background="#222222",
            foreground="#ffffff",
            font=("Cascadia Code", 20, "bold")
        )


class CalcButton(ttk.Button):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text=kwargs["text"],
            command=kwargs["command"]
        )
        
class NumericCalcButton(CalcButton):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text=kwargs["text"],
            command=kwargs["command"]
        )


class WorkingCalcButton(CalcButton):
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text=kwargs["text"],
            command=kwargs["command"]
        )


root = Tk()
# widget settings
root.resizable(False, False)

calc1 = Calc(root)

root.mainloop()