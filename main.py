#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, askokcancel
import random
import string
import os
import pyperclip
import json

WHITE = "#ffffff"
FONT_NAME = "Courier"
password_len = 20


class PasswordManager():
    def __init__(self, root):
        # setup randoms for password generation
        self.char_string = list(string.ascii_letters + string.digits + "!@#$%^&*()")

        # setup windows
        root.title("Brian's Password Manager")
        self.mainframe = ttk.Frame(root, padding='50 50 50 50')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.title = Label(text='YAPM:', font=(FONT_NAME, 20, 'bold'))
        self.title.grid(row=0, column=0)
        self.title2 = Label(text="Brian's Yet Another Password Manager", font=(FONT_NAME, 12, 'bold'))
        self.title2.grid(row=0, column=1, columnspan=2)
        self.generate_button = ttk.Button(root, text="Generate", command=self.generate)
        self.generate_button.grid(row=3, column=3)
        self.save_button = ttk.Button(root, text="Save", command=self.save_password)
        self.save_button.grid(row=4, column=3)
        self.show_button = ttk.Button(root, text="Show", command=self.show_password)
        self.show_button.grid(row=5, column=3)
        self.site_entry = Entry(width=40)
        self.site_entry.insert(0, string="")
        self.site_entry.grid(row=3, column=1, columnspan=2)
        self.login_entry = Entry(width=40)
        self.login_entry.insert(0, string="")
        self.login_entry.grid(row=4, column=1, columnspan=2)
        self.password_entry = Entry(width=40)
        self.password_entry.insert(0, string="")
        self.password_entry.grid(row=5, column=1, columnspan=2)
        self.url_list = Listbox(height=len(self.get_site_list())+10, width=45)
        self.site_list_index = 0
        for site in self.get_site_list():
            self.url_list.insert(self.site_list_index, site)
            self.site_list_index += 1
        self.url_list.bind("<<ListboxSelect>>", lambda event: self.listbox_select(self.url_list.get(self.url_list.curselection())))
        self.url_list.grid(row=6, column=0, columnspan=5)
        self.website_label = Label(text="Website    ▶").grid(row=3, column=0)
        self.login_label = Label(text="Login        ▶").grid(row=4, column=0)
        self.password_label = Label(text="Password  ▶").grid(row=5, column=0)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=20, pady=20)

        self.password_entry.focus()
        root.bind("<Return>", self.generate)

    def popup_error(self, error_string):
        showerror(title="Error", message=f"Error: {error_string}")

    def generate(self):
        global password_len
        random.shuffle(self.char_string)
        self.temp_pw = []
        self.new_pw = ""
        for i in range(password_len):
            self.temp_pw.append(random.choice(self.char_string))
        random.shuffle(self.temp_pw)
        self.new_pw = "".join(self.temp_pw)
        pyperclip.copy(self.new_pw)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, string=self.new_pw)

    def get_site_list(self):
        with open("data.json", "r") as json_file:
            self.json_file_data = json.load(json_file)
        return self.json_file_data.keys()

    def save_password(self):
        self.current_site = self.site_entry.get()
        self.current_login = self.login_entry.get()
        self.current_password = self.password_entry.get()
        self.current_data_json = {
            self.current_site: {
            "login": self.current_login,
            "password": self.current_password
            }
        }
        if self.current_site == "" or self.current_login == "" or self.current_password == "":
            self.popup_error("Please enter all three fields")
        else:
            is_ok = askokcancel(title=self.current_site,
                                message=f"Press OK to save.\n\n"
                                        f"Site: {self.current_site}\n"
                                        f"Login: {self.current_login}\n"
                                        f"PW: {self.current_password}")
            if is_ok:
                try:
                    with open("data.json", "r") as json_file:
                        self.json_file_data = json.load(json_file)
                except FileNotFoundError:
                    self.popup_error("File not found. Creating!")
                    with open("data.json", "a") as json_file:
                        json.dump(self.current_data_json, json_file, indent=4)
                else:
                    self.json_file_data.update(self.current_data_json)
                    with open("data.json", "w") as json_file:
                        json.dump(self.json_file_data, json_file, indent=4)
                finally:
                    self.python = sys.executable
                    os.execl(self.python, self.python, * sys.argv)

    def listbox_select(self, listbox_select_site):
        with open("data.json", "r") as json_file:
            self.json_file_data = json.load(json_file)
        print(type(self.json_file_data))
        if listbox_select_site in self.json_file_data:
            login = self.json_file_data[listbox_select_site]['login']
            password = self.json_file_data[listbox_select_site]['password']
        self.site_entry.delete(0, END)
        self.site_entry.insert(0, listbox_select_site)
        self.login_entry.delete(0, END)
        self.login_entry.insert(0, login)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

    def show_password(self):
        pass


root = Tk()
pm = PasswordManager(root)
root.mainloop()
