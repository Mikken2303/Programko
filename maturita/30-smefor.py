from tkinter import *
from turtle import fillcolor

w = 250
h = 700
canvas = Canvas(width=w, height=h,bg="black")
canvas.pack()

canvas.create_oval(25,25,225,225,fill="dark red")
canvas.create_oval(25,250,225,450,fill="#964B00")
canvas.create_oval(25,475,225,675,fill="dark green")
while True:
    r = canvas.create_oval(25,25,225,225,fill="red")
    canvas.update()
    canvas.after(1000,)
    canvas.delete(r)
    canvas.update()
    y = canvas.create_oval(25,250,225,450,fill="yellow")
    canvas.update()
    canvas.after(250, )
    canvas.delete(y)
    canvas.update()
    g = canvas.create_oval(25,475,225,675,fill="#00FF00")
    canvas.update()
    canvas.after(1000, )
    canvas.delete(g)
    canvas.update()
    y2 = canvas.create_oval(25,250,225,450,fill="yellow")
    canvas.update()
    canvas.after(250, )
    canvas.delete(y2)
    canvas.update()
canvas.mainloop()
