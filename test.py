#only layout, no functionality

import unittest
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
root.title('PhosmaBank')
root.geometry("800x500")

#use tk.Canvas and tk.Frame to make this prettier when you can ok me?
#find out how to change fontsize 2 relative size
label = tk.Label(root, text="Welcome to the PhosmaBank App!\nYour money is as hidden as a ghost!", font=('Courier New', 12))
label.pack(padx=20, pady=20)

#fix scaling + functionality
userbox = tk.Entry(root)
userbox.pack(pady=5)
passbox = tk.Entry(root)
passbox.pack(pady=5)

#buttons. wish i could use bootstrap so i could make them go side by side or on top of one another depending on the viewport easier...
btnacc = tk.Button(root, text="Create Account", font=('Courier New', 12))
btnlogin = tk.Button(root, text="Enter", font=('Courier New', 12))
btnexit = tk.Button(root, text="Exit", font=('Courier New', 12))
#for this do tk.destroy.

btnacc.pack(pady=5)
btnlogin.pack(pady=5)
btnexit.pack(pady=5)



root.mainloop()
