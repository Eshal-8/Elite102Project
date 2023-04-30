#hello world! here's my banking project ig.

#PAGE LAYOUT:
#   1: start page with login ("user has been registered" and "invalid password/login" message conditional pop-up)
#   2: menu for people who are logged in, to deposit, withdraw, and change account details. balance is shown in bottom middle.
#   3: deposit/withdraw menu (differentiated by a variable)
#   5: change account details (add optional first and last name.)
#       JK no page five because thats TOO MUCH WORK!!

import tkinter as tk
from decimal import Decimal
import mysql.connector
pagenum = 1

connection = mysql.connector.connect(user = 'root', password = 'Magic', 
                                     host = 'localhost', 
                                     port = '3306',
                                     database = 'phosmabank')
cursor = connection.cursor()

bodytext1 = ('Courier New', 12)
bodytext2 = ('Courier New', 11)

#i hate variable bloat so much. i'm good with local variables in c but python?!?! what the heck is going on?!??!??
#since im not familiar with local variables in python im... just gonna save these as globals. sorry
user = [0,'','','0.00']
loginstatus = 0
moneystatus = 0
mode = 0
    #= 0: deposit
    #= 1: withdraw
moneyinput = ""

class page1(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global u_user

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="Welcome to the PhosmaBank App!\nYour money is as hidden as a ghost!", font=bodytext1)
        label.grid(column=1, row=0)

        u_user1 = tk.StringVar()
        u_user2 = tk.StringVar()

        userlabel = tk.Label(root, text="Username",padx=5,font=bodytext2)
        userlabel.grid(column=0,row=1,rowspan=2)
        userbox = tk.Entry(root, textvariable=u_user1)
        userbox.grid(column=1,row=1,sticky='nesw',padx=3,pady=3)
        passlabel = tk.Label(root, text="Password",padx=5,font=bodytext2)
        passlabel.grid(column=0,row=3,rowspan=2)
        passbox = tk.Entry(root,show='*',textvariable=u_user2)
        passbox.grid(column=1,row=3,sticky='nesw',padx=3,pady=3)
        #rowspan is not working i give up

        btnacc = tk.Button(root, text="Create Account", command=(lambda: createacc(u_user1,u_user2)), font=bodytext2)
        btnlogin = tk.Button(root, text="Log In", command=(lambda: login(u_user1,u_user2)), font=bodytext2)
        btnexit = tk.Button(root, text="Exit", command=root.destroy, font=bodytext2)
        btnexit.grid(column=0,row=5)
        btnacc.grid(column=1,row=5,sticky='w')
        btnlogin.grid(column=1,row=5,sticky='e')

        bottomtrim = tk.Label(root, text="👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻",font=bodytext1)
        bottomtrim.grid(column=1,row=6)

        statusmessage = tk.Label(root, font=bodytext1)

        if loginstatus == 0:
            pass
        elif loginstatus == 1:
            statusmessage.config(text="Username/password incorrect.")
        elif loginstatus == 2:
            statusmessage.config(text="Username invalid or already exists.")
        elif loginstatus == 3:
            statusmessage.config(text="Password cannot be blank!")
        else:
            statusmessage.config(text="Account successfully created!")

        statusmessage.grid(column=1,row=7)

        bottomtrim = tk.Label(root, text="👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻",font=bodytext1)
        bottomtrim.grid(column=1,row=6)

        btngotest = tk.Button(root, text="Proceed without logging in! (Debug)", command=(lambda: debugpass()), font=bodytext2)
        btngotest.grid(column=1,row=8)

class page2(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global user

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text=f"Hello, {user[1]}!\nYour balance: {user[3]}", font=bodytext1)
        label.grid(column=1, row=0, sticky='nesw')

        btnout = tk.Button(root,text="Withdraw", command = (lambda: changepage(3,1)), font=bodytext1)
        btnin = tk.Button(root,text="Deposit", command = (lambda: changepage(3,0)), font=bodytext1)
        btnout.grid(column=1, row=3, sticky='w')
        btnin.grid(column=1, row=3, sticky='e')
        btnlogout = tk.Button(root, text="Log Out", command=(lambda: logout()), font=bodytext2)
        btnexit = tk.Button(root, text="Exit", command=root.destroy, font=bodytext2)
        btnlogout.grid(column=1, row=4, sticky='w')
        btnexit.grid(column=1, row=4, sticky='e')

        bottomtrim = tk.Label(root, text="👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻~👻",font=bodytext1)
        bottomtrim.grid(column=1,row=6)

        statusmessage = tk.Label(root, font=bodytext1)

        if moneystatus == 0:
            pass
        elif moneystatus == 1:
            statusmessage.config(text="Change could not be committed\nto database. Updated locally.")

        statusmessage.grid(column=1,row=7)
        

class page3(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global moneyinput

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="DEPOSIT AMOUNT", font=bodytext1)
        if mode:
            label.config(text="WITHDRAW AMOUNT")
        label.grid(column=1,row=0)

        inputdisplay = tk.Label(root, text=moneyinput, font=bodytext1)
        inputdisplay.grid(column=1,row=1)
        #inputdisplay.config(state='disabled')

        num1 = tk.Button(root, text="1", command=(lambda: press(1)), height=1, width=3, font=bodytext1)
        num2 = tk.Button(root, text="2", command=(lambda: press(2)), height=1, width=3, font=bodytext1)
        num3 = tk.Button(root, text="3", command=(lambda: press(3)), height=1, width=3, font=bodytext1)
        num4 = tk.Button(root, text="4", command=(lambda: press(4)), height=1, width=3, font=bodytext1)
        num5 = tk.Button(root, text="5", command=(lambda: press(5)), height=1, width=3, font=bodytext1)
        num6 = tk.Button(root, text="6", command=(lambda: press(6)), height=1, width=3, font=bodytext1)
        num7 = tk.Button(root, text="7", command=(lambda: press(7)), height=1, width=3, font=bodytext1)
        num8 = tk.Button(root, text="8", command=(lambda: press(8)), height=1, width=3, font=bodytext1)
        num9 = tk.Button(root, text="9", command=(lambda: press(9)), height=1, width=3, font=bodytext1)
        num0 = tk.Button(root, text="0", command=(lambda: press(0)), height=1, width=3, font=bodytext1)
        numd = tk.Button(root, text=".", command=(lambda: press('d')), height=1, width=3, font=bodytext1)
        nums = tk.Button(root, text="-", command=(lambda: press('s')), height=1, width=3, font=bodytext1)

        num1.grid(column=1,row=3,sticky='w')
        num2.grid(column=1,row=3)
        num3.grid(column=1,row=3,sticky='e')
        num4.grid(column=1,row=4,sticky='w')
        num5.grid(column=1,row=4)
        num6.grid(column=1,row=4,sticky='e')
        num7.grid(column=1,row=5,sticky='w')
        num8.grid(column=1,row=5)
        num9.grid(column=1,row=5,sticky='e')
        numd.grid(column=1,row=6,sticky='w')
        num0.grid(column=1,row=6)
        nums.grid(column=1,row=6,sticky='e')

        back = tk.Button(root, text="Back", command=(lambda:clearminput()), font=bodytext1)
        go = tk.Button(root, text="Go", command=(lambda:alterbalance()), font=bodytext1)

        back.grid(column=1,row=7,sticky='w')
        go.grid(column=1,row=7,sticky='e')

class pageerror(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        emojilabel = tk.Label(root, text="👻", font=('Courier New', 20))
        emojilabel.grid(column=0,row=0)
        label = tk.Label(root, text="This is the silly error page!!\nThis means that I probably messed something up.", font=bodytext1)
        label.grid(column=1, row=0)


def press(num):
    global moneyinput

    if num == 's':
        moneyinput = moneyinput[:-1]

    if len(moneyinput) > 1 and moneyinput.find(".") != -1:
        d = Decimal(f'{moneyinput}')
        if d.as_tuple().exponent < -1:
            changepage(3,mode)
    
    if len(moneyinput) <= 30:
        if type(num) == int:
            moneyinput = moneyinput + str(num)
        elif num == 'd' and moneyinput.find(".") == -1:
            moneyinput = moneyinput + "."
        changepage(3,mode)

def alterbalance():
    global moneyinput, moneystatus

    m = Decimal('0.0')
    u_moneyinput = Decimal(moneyinput)
    cursor.execute(f"SELECT balance FROM userinfo WHERE username = '{user[1]}'")
    for i in cursor:
        m = Decimal(i[0])

    print(moneyinput, m)

    if mode:
        u_moneyinput = m - u_moneyinput
    else:
        u_moneyinput = m + u_moneyinput

    print(u_moneyinput)
    cursor.execute(f"UPDATE userinfo SET balance ='{u_moneyinput}' WHERE username = '{user[1]}'")
    user[3] = u_moneyinput
    moneyinput = ""

    if cursor.rowcount != 1:
        moneystatus = 1
        changepage(2,0)

    connection.commit()
    changepage(2,0)

def clearminput():
    global moneyinput
    moneyinput = ""
    changepage(2,0)


def login(u_user1, u_user2):
    #function purpose: check username and password to match with database. if match, sign in under that id number. if not, return invalid and send back to page 1.
    global loginstatus, user

    user[1] = u_user1.get()
    user[2] = u_user2.get()

    _existinguser = []
    cursor.execute(f"SELECT id, username, password, balance FROM userinfo WHERE username = '{user[1]}' AND password = '{user[2]}'")
    for i in cursor:
        _existinguser.append(i)

    if len(_existinguser) > 0:
        user = [_existinguser[0][0],f"{user[1]}",f"{user[2]}",_existinguser[0][3]]
        changepage(2,0)
    else:
        loginstatus = 1
        #print(u_user1, u_user2)
        #print(_input)
        changepage(1,0)
        return

def createacc(u_user1, u_user2):
    #function purpose: check if username isn't taken and properly assign username and password. if username is already taken, return invalid and send back to page 1.
    global loginstatus, user

    _user1 = u_user1.get()
    _user2 = u_user2.get()

    #i'd like to sanitize the input but. i can only do the bare minimum at the moment unfortunately :(
    #sighh i love arrays <3 ig these are lists but still. yes im a c bootlicker idc that its inefficient
    _existinguser = []
    cursor.execute(f"SELECT username FROM userinfo WHERE username = '{_user1}'")
    for i in cursor:
        _existinguser.append(i)

    print(_user1, _existinguser)
    if _user2 == '':
        loginstatus = 3
    elif (_user1 == '') or (_existinguser != []):
        loginstatus = 2
    else:
        user[1] = _user1
        user[2] = _user2
        cursor.execute(f"INSERT INTO userinfo (username,password) VALUES ('{user[1]}','{user[2]}')")
        connection.commit()
        loginstatus = 4
    changepage(1,0)

def debugpass():
    global user
    user = [0, 'Ghost', 'password', '0.00']
    changepage(2,0)

def logout():
    user = [0,'','',0]
    loginstatus = 0
    changepage(1,0)

#ooof super clumsy way of doing this, but whatever.
def changepage(pagenum,u_mode):
    global root, main, mode
    for widget in root.winfo_children():
        widget.destroy()

    mode = u_mode

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
    else:
        main = pageerror(root)

    root.mainloop()

root = tk.Tk()
main = page1(root)
main.grid(sticky='nsew')
root.wm_geometry("450x300")
root.title('PhosmaBank')
root.mainloop()