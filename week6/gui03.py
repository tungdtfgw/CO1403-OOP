from tkinter import *
from tkinter import messagebox as msb

from gui_base import BaseGUI

class GUI03(BaseGUI):
    def __init__(self):
        super().__init__("GUI 03", 400, 300)

    # override create_widgets method
    def create_widgets(self):
        lbl_salary = Label(self.window, text="Salary:")
        lbl_salary.grid(row=0, column=0, padx=10, pady=10)

        self.salary = StringVar()
        self.txt_salary = Entry(self.window, textvariable=self.salary) # assign the Entry widget to salary
        self.txt_salary.grid(row=0, column=1, padx=10, pady=10)
        
        lbl_tax = Label(self.window, text="Tax Rate (%):")
        lbl_tax.grid(row=1, column=0, padx=10, pady=10)

        self.tax_rate = StringVar()
        self.txt_tax = Entry(self.window, textvariable=self.tax_rate)
        self.txt_tax.grid(row=1, column=1, padx=10, pady=10)

        btn_calculate = Button(self.window, text="Calculate Salary", command=self.calculate_salary)
        btn_calculate.grid(row=2, column=1, padx=10, pady=10)
    
    # event-handler
    def calculate_salary(self):
        # get the salary and tax rate from the Entry widgets
        salary = float(self.salary.get())
        tax_rate = float(self.tax_rate.get())
        # calculate the net salary
        net_salary = salary * (1 - tax_rate / 100)
        # show the result in a messagebox
        msb.showinfo("Net Salary", f"Net Salary: {net_salary:.2f}")

# Main program
if __name__ == "__main__":
    program = GUI03()
    program.run()