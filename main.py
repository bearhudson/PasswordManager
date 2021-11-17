#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

WHITE = "#ffffff"
FONT_NAME = "Courier"


class PasswordManager:
    def __init__(self, root):
        root.title("Password Manager")
        mainframe = ttk.Frame(root, padding='5 5 10 10')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.title = Label(text='Password Manager', font=(FONT_NAME, 20, 'bold'))
        self.title.grid(row=0, column=1)
        self.canvas = Canvas(width=600, height=600, highlightthickness=0)
        self.lock_image = PhotoImage(file="padlock.png")
        self.canvas.create_image(300, 220, image=self.lock_image)
        self.canvas.grid(row=1, column=1)
        self.password_text = Label(text='Password: ', font=(FONT_NAME, 12, 'bold'))
        self.password_text.grid(row=2, column=0)
        self.password_entry = Entry(width=50)
        self.password_entry.insert(END, string='Passwords')
        self.password_entry.grid(row=2, column=1)


root = Tk()
pm = PasswordManager(root)
root.mainloop()
