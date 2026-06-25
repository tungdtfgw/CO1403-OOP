from tkinter import *
from tkinter import messagebox as msb

class BaseGUI:
    def __init__(self, title, width, height):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

        self.create_widgets()

    def create_widgets(self):
        pass


    def run(self):
        self.window.mainloop()