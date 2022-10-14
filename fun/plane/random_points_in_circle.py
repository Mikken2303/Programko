from math import *
from tkinter import *
from random import *
main = Tk()
canvas = Canvas()
canvas_width = 1000
canvas_height = 1000
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

radius = 25
coords = (500,500)
def rock(radius,coords):
    points = []
    for i in range(0,5):
        r = radius * sqrt(random())
        theta = random() * 2 * pi
        x = coords[0] + r * cos(theta)
        y = coords[1] + r * sin(theta)
        points.append((int(x),int(y)))

    canvas.create_polygon(points,fill="black")



mainloop()