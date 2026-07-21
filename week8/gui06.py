from tkinter import *
from tkinter import messagebox as msb
from book import Book

from gui_base import BaseGUI

class GUI06(BaseGUI):
    def __init__(self, title, width, height):
        super().__init__(title, width, height)
        self.load_books()
    
    def load_books(self):
        self.books = []

        python_intro = Book("Python Introduction", "John Smith", 100)
        self.books.append(python_intro)

        java_intro = Book("Java Introduction", "Jane Doe", 120)
        self.books.append(java_intro)

        c_sharp_intro = Book("C# Introduction", "Jim Beam", 130)
        self.books.append(c_sharp_intro)

        # add books' titles to the listbox
        for book in self.books:
            self.lst_books.insert(END, book.title)

    def create_widgets(self):
        lbl_book = Label(self.window, text="All Books")
        lbl_book.grid(row=0, column=0, sticky=W, pady=10, padx=10)

        # selectmode=SINGLE: only one item can be selected at a time
        # exportselection=0: prevent the selection from being exported to other widgets
        self.lst_books = Listbox(self.window, selectmode=SINGLE, exportselection=0)
        self.lst_books.grid(row=1, column=0, sticky=W, pady=10, padx=10, rowspan=4)
        # bind listbox selection to a function
        self.lst_books.bind("<<ListboxSelect>>", self.lst_books_selected)
        lbl_title = Label(self.window, text="Title")
        lbl_title.grid(row=1, column=1, sticky=E, pady=10, padx=10)

        self.title = StringVar()
        txt_title = Entry(self.window, textvariable=self.title)
        txt_title.grid(row=1, column=2, sticky=W, pady=10, columnspan=3, padx=10)

        lbl_author = Label(self.window, text="Author")
        lbl_author.grid(row=2, column=1, sticky=E, pady=10, padx=10)

        self.author = StringVar()
        txt_author = Entry(self.window, textvariable=self.author)
        txt_author.grid(row=2, column=2, sticky=W, pady=10, columnspan=3, padx=10)

        lbl_price = Label(self.window, text="Price")
        lbl_price.grid(row=3, column=1, sticky=E, pady=10, padx=10)
        
        self.price = StringVar()
        txt_price = Entry(self.window, textvariable=self.price)
        txt_price.grid(row=3, column=2, sticky=W, pady=10, columnspan=3, padx=10)

        btn_add = Button(self.window, text="Add", command=self.btn_add_clicked)
        btn_add.grid(row=4, column=2, sticky=W, pady=10, padx=10)

        btn_update = Button(self.window, text="Edit", command=self.btn_update_clicked)
        btn_update.grid(row=4, column=3, sticky=W, pady=10, padx=10)

        btn_delete = Button(self.window, text="Del", command=self.btn_delete_clicked)
        btn_delete.grid(row=4, column=4, sticky=W, pady=10, padx=10)
    
    def lst_books_selected(self, event):
        # get the selected index from the listbox
        position = self.lst_books.curselection()[0]

        # get the selected book from the books list
        book = self.books[position]

        # set book's attributes to the entry widgets
        self.title.set(book.title)
        self.author.set(book.author)
        self.price.set(book.price)
    
    def btn_add_clicked(self):
        title = self.title.get()
        author = self.author.get()
        price = self.price.get()
        # validate empty fields
        if title == "" or author == "" or price == "":
            msb.showerror("Error", "Please fill in all fields")
            return
        # validate price is a number
        try:
            price = int(price)
        except ValueError:
            msb.showerror("Error", "Price must be a number")
            return
        # create a new book object
        book = Book(title, author, price)
        self.books.append(book) # add the new book to the books list
        self.lst_books.insert(END, book.title) # add the new book's title to the listbox
    
    def btn_update_clicked(self):
        # get the selected index from the listbox
        position = self.lst_books.curselection()[0]
        # get the selected book from the books list
        book = self.books[position]
        # update the book's attributes
        book.title = self.title.get()
        book.author = self.author.get()
        book.price = self.price.get()
        # update the book's attributes in the listbox
        self.lst_books.delete(position)
        self.lst_books.insert(position, book.title)

    def btn_delete_clicked(self):
        # get the selected index from the listbox
        position = self.lst_books.curselection()[0]
        # delete from the books list
        del self.books[position]
        # delete from the listbox
        self.lst_books.delete(position)

if __name__ == "__main__":
    gui = GUI06("Book Management System", 600, 400)
    gui.run()