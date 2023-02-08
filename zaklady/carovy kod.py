from tkinter import *
from random import *
canvas = Canvas(width=400, height=250,bg="white")
canvas.pack()

canvas.create_line(25,0,25,250,width=randint(1,9))
canvas.create_line(375,0,375,250,width=randint(1,9))
for i in range(0,6):
    r = randint(0, 9)
    canvas.create_line(75+50*i, 0, 75+50*i, 200, width=r)
    canvas.create_text(75+50*i,225,text=r)
canvas.mainloop()