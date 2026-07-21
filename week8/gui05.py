from tkinter import *
from tkinter import messagebox as msb

from gui_base import BaseGUI

class GUI05(BaseGUI):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)

    def create_widgets(self):
        lbl_title = Label(self.window, text="Chương trình tính lương")
        lbl_title.grid(row=0, column=0, columnspan=3, sticky=EW, pady=10)
        
        lbl_salary = Label(self.window, text="Lương:")
        lbl_salary.grid(row=1, column=0, sticky=E, pady=10)

        self.salary = StringVar()
        txt_salary = Entry(self.window, textvariable=self.salary)
        txt_salary.grid(row=1, column=1, sticky=W, pady=10, columnspan=2)

        lbl_allowance = Label(self.window, text="Phụ cấp:")
        lbl_allowance.grid(row=2, column=0, sticky=E, pady=10)

        self.allowance = StringVar()
        txt_allowance = Entry(self.window, textvariable=self.allowance)
        txt_allowance.grid(row=2, column=1, sticky=W, pady=10, columnspan=2)

        lbl_dependents = Label(self.window, text="Người phụ thuộc:")
        lbl_dependents.grid(row=3, column=0, sticky=E, pady=10)

        self.dependents = IntVar()
        rd_dependent_yes = Radiobutton(self.window, text="Có", value=1, variable=self.dependents)
        rd_dependent_yes.grid(row=3, column=1, sticky=E, pady=10)
        rd_dependent_no = Radiobutton(self.window, text="Không", value=0, variable=self.dependents)
        rd_dependent_no.grid(row=3, column=2, sticky=E, pady=10)

        btn_calculate = Button(self.window, text="Tính lương", command=self.calculate_salary)
        btn_calculate.grid(row=4, column=1, columnspan=2, sticky=EW, pady=10)

        lbl_tax = Label(self.window, text="Thuế:")
        lbl_tax.grid(row=5, column=0, sticky=E, pady=10)

        self.tax = StringVar()
        txt_tax = Entry(self.window, textvariable=self.tax)
        txt_tax.grid(row=5, column=1, sticky=W, pady=10, columnspan=2)

        lbl_actual_salary = Label(self.window, text="Lương thực lĩnh:")
        lbl_actual_salary.grid(row=6, column=0, sticky=E, pady=10)

        self.actual_salary = StringVar()
        txt_actual_salary = Entry(self.window, textvariable=self.actual_salary)
        txt_actual_salary.grid(row=6, column=1, sticky=W, pady=10, columnspan=2)

    def calculate_salary(self):
        try:
            # Read data (salary, allowance, dependents)
            salary = int(self.salary.get())
            allowance = int(self.allowance.get())
            has_dependents = True if self.dependents.get() == 1 else False
        except ValueError:
            msb.showerror("Lỗi", "Vui lòng nhập số lương và phụ cấp hợp lệ")
            return
        total_salary = salary + allowance
        if has_dependents:
            tax_deduction = total_salary - 6000000
        else:
            tax_deduction = total_salary

        tax = tax_deduction * 0.1
        actual_salary = total_salary - tax
        self.tax.set(tax)
        self.actual_salary.set(actual_salary)

# Main
if __name__ == "__main__":
    app = GUI05("Chương trình tính lương", 300, 200)
    app.run()