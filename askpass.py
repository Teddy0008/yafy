#!/usr/bin/env python
import tkinter
from tkinter import ttk
import os

import screeninfo
from screeninfo import *

for i in screeninfo.get_monitors():
    if i.is_primary == True:
        scrWidth = i.width
        scrHeight = i.height
def setPwd():
    passwd = pwdInput.get()
    print(passwd)
    root.destroy()

root = tkinter.Tk()
root.geometry(f"{int(scrWidth * 0.2)}x{int(scrHeight * 0.1)}")

pwdEnterText = ttk.Label(root, text="Please enter your password", font=("", int(scrWidth * 0.007)))
pwdEnterText.pack()

pwdInput = ttk.Entry(root, width=int(scrWidth * 0.017), font=("", int(scrWidth * 0.008)), show="*")
pwdInput.pack()

okButton = tkinter.Button(root, text="Ok", command=setPwd, font=("", int(scrWidth * 0.007)), width=int(scrWidth * 0.003))
okButton.pack(side="right", padx=f"{int(scrWidth * 0.007)}")



root.mainloop()