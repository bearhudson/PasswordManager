#!/usr/bin/python3

from tkinter import *
from tkinter import ttk

WHITE = "#ffffff"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)
title = Label(text='Password Manager', font=(FONT_NAME, 20, 'bold'))
title.grid(row=0, column=1)
canvas = Canvas(width=600, height=600, highlightthickness=0)
lock_image = PhotoImage(file="padlock.png")
canvas.create_image(300, 220, image=lock_image)
canvas.grid(row=1, column=1)
password_text = Label(text='Password: ', font=(FONT_NAME, 12, 'bold'))
password_text.grid(row=2, column=0)
password_entry = Entry(width=50)
password_entry.insert(END, string='Passwords')
password_entry.grid(row=2, column=1)

window.mainloop()