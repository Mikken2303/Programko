from math import *
from tkinter import *
from random import *
main = Tk()
canvas = Canvas()
canvas_width = 1000
canvas_height = 1000
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

def rock(radius,coords):
    points = []
    for i in range(0,5):
        r = radius * sqrt(random())
        theta = random() * 2 * pi
        x = coords[0] + r * cos(theta)
        y = coords[1] + r * sin(theta)
        points.append((int(x),int(y)))
    canvas.create_polygon(points,fill="black")

def plane(crds):
    p1 = (crds[0],crds[1] - 10)
    p2 = (crds[0] - 25 ,crds[1] + 10)
    p3 = (crds[0] - 10 ,crds[1] + 5)
    p4 = (crds[0] - 10 ,crds[1] + 25)
    p5 = (crds[0],crds[1] +7)
    p6 = (crds[0] + 10 ,crds[1] + 25)
    p7 = (crds[0] + 10 ,crds[1] + 5)
    p8 = (crds[0] + 25 ,crds[1] + 10)

    canvas.create_polygon(p1,p2,p3,p4,p5,p6,p7,p8, fill="black")


mainloop()