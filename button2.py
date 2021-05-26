from tkinter import *

p = Tk()

Btn1 = Button(p, text="Bluebtn", fg = "Blue")
Btn1.pack(side = LEFT)

Btn2 = Button(p, text="Blackbtn", fg = "Black")
Btn2.pack(side = RIGHT)

Btn3 = Button(p, text="Redbtn", fg = "Red")
Btn3.pack(side = TOP)

p.mainloop()
