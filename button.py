import tkinter
from tkinter import *

p = tkinter.Tk()

p.geometry("250x250")
btn = Button(p, text="Button 1")
btn2 = Button(p, text="button2")

btn.pack()
btn2.pack()

p.mainloop()