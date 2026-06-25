from tkinter import *
from tkinter import messagebox as msb

from gui_base import BaseGUI

class GUI04(BaseGUI):
    def __init__(self):
        super().__init__("GUI 04", 300, 300)

    def create_widgets(self):
        lbl_combo = Label(self.window, text="Select a combo:")
        lbl_combo.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.combo_var = IntVar()
        self.combo_var.set(1)  # Set default value
        rd_pizza = Radiobutton(self.window, text="Pizza", value=1, variable=self.combo_var, 
                            command=self.rd_combo_click)
        rd_pizza.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        rd_burger = Radiobutton(self.window, text="Burger", value=2, variable=self.combo_var,
                                command=self.rd_combo_click)
        rd_burger.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        rd_sushi = Radiobutton(self.window, text="Sushi", value=3, variable=self.combo_var,
                                command=self.rd_combo_click)
        rd_sushi.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        lbl_payment = Label(self.window, text="Payment:")
        lbl_payment.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.payment_var = StringVar()
        self.payment_var.set("$10")  # Set default payment value
        txt_payment = Entry(self.window, textvariable=self.payment_var)
        txt_payment.grid(row=5, column=0, padx=10, pady=5, sticky=W)
    
    def rd_combo_click(self):
        # get the selected combo value
        selected_combo = int(self.combo_var.get())
        if selected_combo == 1:
            self.payment_var.set("$10")
        elif selected_combo == 2:
            self.payment_var.set("$8")
        elif selected_combo == 3:
            self.payment_var.set("$12")

## Main program
if __name__ == "__main__":
    program = GUI04()
    program.run()