#!/usr/bin/python3

from tkinter import *
from tkinter import ttk


class PasswordManager:

    def __init__(self, root):
        root.title("Password Manager")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.password = StringVar()
        password_entry = ttk.Entry(mainframe, width=7, textvariable=self.password)
        password_entry.grid(column=2, row=1, sticky=(W, E))

        self.kilometers = StringVar()
        ttk.Label(mainframe, textvariable=self.kilometers).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Save", command=self.save).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="Password").grid(column=3, row=1, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        password_entry.focus()
        root.bind("<Return>", self.save)

    def save(self, *args):
        try:
            value = self.password.get()
            print(value)
        except ValueError:
            pass


root = Tk()
PasswordManager(root)
root.mainloop()
