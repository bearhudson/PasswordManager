#!/usr/bin/python3
import tkinter
from tkinter import *
from tkinter import ttk
import random
import string

WHITE = "#ffffff"
FONT_NAME = "Courier"
password_len = 20


class PasswordManager:
    def __init__(self, root):
        # setup randoms for password generation
        self.char_string = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        # setup windows
        root.title("Aniki's Password Manager")
        self.mainframe = ttk.Frame(root, padding='10 10 10 10')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.title = Label(text='YAPM:', font=(FONT_NAME, 20, 'bold'))
        self.title.grid(row=0, column=1)
        self.title = Label(text='Aniki\'s Yet Another Password Manager', font=(FONT_NAME, 12, 'bold'))
        self.title.grid(row=1, column=1, columnspan=2)
        self.canvas = Canvas()
        # self.lock_image = PhotoImage(file="tiny_lock.png")
        # self.canvas.create_image(50, 50, image=self.lock_image)
        # self.canvas.grid(row=2, column=1, columnspan=1, rowspan=1)
        self.generate_button = ttk.Button(root, text="Generate", command=self.generate)
        self.generate_button.grid(row=3, column=1)
        self.save_button = ttk.Button(root, text="Save", command=self.save_password)
        self.save_button.grid(row=4, column=1)
        self.site_entry = Entry(width=40)
        self.site_entry.insert(END, string='Website')
        self.site_entry.grid(row=5, column=1)
        self.login_entry = Entry(width=40)
        self.login_entry.insert(END, string='Login')
        self.login_entry.grid(row=6, column=1)
        self.password_entry = Entry(width=40)
        self.password_entry.insert(END, string='Password')
        self.password_entry.grid(row=7, column=1)
        self.url_list = StringVar()
        self.url_list_box = tkinter.Text(height=30, width=60)
        self.url_list_box.grid(row=8, column=1)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=20, pady=20)

        self.password_entry.focus()
        root.bind("<Return>", self.generate)

    def generate(self):
        global password_len
        random.shuffle(self.char_string)
        self.temp_pw = []
        self.new_pw = ""
        for i in range(password_len):
            self.temp_pw.append(random.choice(self.char_string))
        random.shuffle(self.temp_pw)
        self.new_pw = "".join(self.temp_pw)
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, string=self.new_pw)

    def save_password(self):
        self.current_site = self.site_entry.get()
        self.current_login = self.login_entry.get()
        self.current_password = self.password_entry.get()
        if self.current_site == "" or self.current_login == "" or self.current_password == "":
            self.popup_error("Please enter all three fields")
        else:
            print(self.current_site)
            print(self.current_login)
            print(self.current_password)

    def popup_error(self, error_string):
        root.showinfo(f"Error: {error_string}")


root = Tk()
pm = PasswordManager(root)
root.mainloop()
