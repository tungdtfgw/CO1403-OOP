from tkinter import *
from tkinter import messagebox as msb

# Create the main window
window = Tk()
window.title("Simple GUI")
window.geometry("300x200")

# Event-handler function for button click
def button_click():
    msb.showinfo("Information", "Button was clicked!")

# Create widgets
label = Label(window, text="Hello, World!")
label.grid(row=0, column=0, padx=10, pady=10)

# create a button, register the event-handler function
button = Button(window, text="Click Me", command=button_click)
button.grid(row=1, column=1, padx=10, pady=10)


# Run the main event loop
window.mainloop()