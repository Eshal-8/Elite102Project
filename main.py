#hello world! here's my banking project ig.

#PAGE LAYOUT:
#   1: start page with login ("user has been registered" and "invalid password/login" message conditional pop-up)
#   2: menu for people who are logged in, to deposit, withdraw, and change account details. balance is shown in bottom middle.
#   3: deposit menu
#   4: withdraw menu
#   5: change account details (add optional first and last name.)

import tkinter as tk
from tkinter import filedialog, Text
import os
import mysql.connector
pagenum = 1

connection = mysql.connector.connect(user = 'root', password = 'Magic', 
                                     host = 'localhost', 
                                     port = '3306',
                                     database = 'phosmabank')

bodytext1 = ('Courier New', 12)
bodytext2 = ('Courier New', 11)

u_username = ''
u_password = ''

class page1(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="Welcome to the PhosmaBank App!\nYour money is as hidden as a ghost!", font=bodytext1)
        label.grid(column=1, row=0)

        u_username = tk.StringVar()
        u_password = tk.StringVar()

        userlabel = tk.Label(root, text="Username",padx=5,font=bodytext2)
        userlabel.grid(column=0,row=1,rowspan=2)
        userbox = tk.Entry(root, textvariable=u_username)
        userbox.grid(column=1,row=1,sticky='nesw',padx=3,pady=3)
        passlabel = tk.Label(root, text="Password",padx=5,font=bodytext2)
        passlabel.grid(column=0,row=3,rowspan=2)
        passbox = tk.Entry(root,show='*',textvariable=u_password)
        passbox.grid(column=1,row=3,sticky='nesw',padx=3,pady=3)

        u_username.get()
        u_password.get()
        #rowspan is not working i give up

        btnacc = tk.Button(root, text="Create Account", font=bodytext2)
        btnlogin = tk.Button(root, text="Log In", command=(lambda: changepage(2)), font=bodytext2)
        btnexit = tk.Button(root, text="Exit", command=root.destroy, font=bodytext2)
        btnexit.grid(column=0,row=5)
        btnacc.grid(column=1,row=5,sticky='w')
        btnlogin.grid(column=1,row=5,sticky='e')

        bottomtrim = tk.Label(root, text="👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻",font=bodytext1)
        bottomtrim.grid(column=1,row=6)

class page2(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="This should be the second page!", font=bodytext1)
        label.grid(column=1, row=0)

class page3(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="This should be the third page!", font=bodytext1)
        label.grid(column=1, row=0)

class page4(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="This should be the fourth page!", font=bodytext1)
        label.grid(column=1, row=0)

class page5(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="This should be the fifth page!", font=bodytext1)
        label.grid(column=1, row=0)

class pageerror(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="Something has gone wrong!", font=bodytext1)
        label.grid(column=1, row=0)

def login():
    #function purpose: check username and password to match with database. if match, sign in under that id number. if not, return invalid and send back to page 1.
    #will use u_username and u_password entered into the box.
    print('hello sillies!')

def createacc():
    #function purpose: check if username isn't taken and properly assign username and password. if username is already taken, return invalid and send back to page 1.
    #will use u_username and u_password entered into the box.
    print('not done with this dumb thing grraaahhh')

#ooof super clumsy way of doing this, but whatever.
def changepage(pagenum):
    global root, main
    for widget in root.winfo_children():
        widget.destroy()
    #DO SWITCH/CASE STATEMENTS NOT EXIST?????? istg time to make the most inefficient code known to man

    #root = tk.Tk()
    #main = page1(root)
    #main.grid(sticky='nsew')
    #root.wm_geometry("450x300")
    #root.title('PhosmaBank')

    if pagenum == 1:
        main = page1(root)
    elif pagenum == 2:
        main = page2(root)
    elif pagenum == 3:
        main = page3(root)
    elif pagenum == 4:
        main = page4(root)
    elif pagenum == 5:
        main = page5(root)
    else:
        main = pageerror(root)

    root.mainloop()

root = tk.Tk()
main = page1(root)
main.grid(sticky='nsew')
root.wm_geometry("450x300")
root.title('PhosmaBank')
root.mainloop()