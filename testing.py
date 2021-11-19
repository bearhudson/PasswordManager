# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# def popup_bonus():
#     win = tk.Toplevel()
#     win.wm_title("Window")
#
#     l = tk.Label(win, text="Input")
#     l.grid(row=0, column=0)
#
#     b = ttk.Button(win, text="Okay", command=win.destroy)
#     b.grid(row=1, column=0)
#
# def popup_showinfo():
#     showinfo("Window", "Hello World!")
#
# class Application(ttk.Frame):
#
#     def __init__(self, master):
#         ttk.Frame.__init__(self, master)
#         self.pack()
#
#         self.button_bonus = ttk.Button(self, text="Bonuses", command=popup_bonus)
#         self.button_bonus.pack()
#
#         self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
#         self.button_showinfo.pack()
#
# root = tk.Tk()
#
# app = Application(root)
#
# root.mainloop()

from tkinter import *

main = Tk()

def onSelection(event):
    widget = event.widget
    return widget.curselection()

someList = ['Stilton', 'Brie', 'Edam', 'Cheddar', 'Ilchester']

chars = Listbox(main)
chars.pack(padx=10, pady=10)
for item in someList:
    chars.insert(0, item)

sam = "sam"
chars.bind("<<ListboxSelect>>", lambda event: print(event.widget.get(event.widget.curselection())))
# Take care of event created by bind ----^                    ^
# Pass the event as well as argument to callback function ----|

main.mainloop()

#---------------------------------------

from tkinter import *

ws = Tk()
ws.title('Python Guides')
ws.geometry('400x300')

var = StringVar()

def showSelected():
    countries = []
    cname = lb.curselection()
    for i in cname:
        op = lb.get(i)
        countries.append(op)
    for val in countries:
        print(val)

show = Label(ws, text = "Select Your Country", font = ("Times", 14), padx = 10, pady = 10)
show.pack()
lb = Listbox(ws, selectmode = "multiple")
lb.pack(padx = 10, pady = 10, expand = YES, fill = "both")

x =["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Australia", "Brazil", "Canada", "China", "Iceland", "Israel", "United States", "Zimbabwe"]

for item in range(len(x)):
	lb.insert(END, x[item])
	lb.itemconfig(item, bg="#bdc1d6")

Button(ws, text="Show Selected", command=showSelected).pack()
ws.mainloop()