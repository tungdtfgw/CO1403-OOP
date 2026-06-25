from tkinter import *
from tkinter import messagebox as msb

from gui_base import BaseGUI

class SimpleGUI(BaseGUI):
    def __init__(self):
        super().__init__("Simple GUI", 300, 200)

    # override create_widgets method
    def create_widgets(self):
        label = Label(self.window, text="Hello, World!")
        label.grid(row=0, column=0, padx=10, pady=10)

        button = Button(self.window, text="Click Me", command=self.button_click)
        button.grid(row=1, column=1, padx=10, pady=10)

    def button_click(self):
        msb.showinfo("Information", "Button was clicked!")

## Main program
if __name__ == "__main__":
    program = SimpleGUI()
    program.run()