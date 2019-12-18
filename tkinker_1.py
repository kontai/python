#!/usr/bin/python3
from tkinter import *

import tkinter.simpledialog as sd
import tkinter.messagebox as mb

root = Tk()
w = Label(root, text="Label Tittle")
w.pack()

mb.showinfo("Welcome", "Welcome Message")
guess = sd.askinteger("Number", "請輸入整數")

output = "This is output message"
mb.showinfo("output視窗 ", output)
