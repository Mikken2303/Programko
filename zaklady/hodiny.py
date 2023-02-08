from tkinter import *
from math import *
canvas = Canvas(width=500, height=500,bg="white")
canvas.pack()

canvas.create_oval(100,100,400,400,)
a = 0
am = 0
#for i in range(1,13):
    #canvas.create_text(250+140*cos((2*pi)/i),250+140*cos((2*pi)/i),text=i)

while True:
    s = canvas.create_line(250,250,250+125*sin(a),250-125*cos(a))
    m = canvas.create_line(250,250,250+100*sin(am),250-100*cos(am))
    a += pi/30

    if round(a,6) == round(2*pi,6):
        print("bleh")
        am += pi / 30
        canvas.delete(m)
        a += - 2*pi
    canvas.update()
    canvas.after(10,)
    canvas.delete(s)
canvas.mainloop()