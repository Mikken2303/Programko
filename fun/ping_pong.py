from tkinter import *
from random import *

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()

r = 5

oval = canvas.create_oval(250-r, 250-r, 250+r, 250+r, fill=("black"))
r_plat = canvas.create_line(100,210,100,290,width="5")
l_plat = canvas.create_line(400,210,400,290,width="5")

def centre_coords(object):
    x = (canvas.coords(object)[0] + canvas.coords(object)[2]) / 2
    y = (canvas.coords(object)[1] + canvas.coords(object)[3]) / 2
    return x,y

vector_x = 1
vector_y = 1

def l_up(sur):
   canvas.move(l_plat,0,-25)
   print(sur)
def l_down(sur):
   canvas.move(l_plat,0,25)
   print(sur)

def r_up(sur):
    canvas.move(r_plat,0,-25)
    print(sur)
def r_down(sur):
    canvas.move(r_plat,0, 25)
    print(sur)

def check_if_outbounds(plat):
    if centre_coords(plat)[1] > 500:
        canvas.move(plat,0,-520)
    elif centre_coords(plat)[1] < 0:
        canvas.move(plat, 0, 520)


while True:
    root.bind("<Up>", l_up)
    root.bind("<Down>", l_down)
    root.bind("<w>", r_up)
    root.bind("<s>", r_down)
    canvas.after(1,)
    canvas.update()
    canvas.move(oval, vector_x,vector_y)
    check_if_outbounds(l_plat)
    check_if_outbounds(r_plat)


# to do points system
    if canvas.coords(oval)[0] > 500 or canvas.coords(oval)[0] < 0:
        vector_x = -vector_x
    if canvas.coords(oval)[0] < 0:
        vector_x = -vector_x

    if canvas.coords(oval)[1] > 500 or canvas.coords(oval)[1] < 0:
        vector_y= -vector_y

    if int(centre_coords(oval)[0] - 5) == int(centre_coords(r_plat)[0]) and int(canvas.coords(oval)[1]) > int(canvas.coords(r_plat)[1]) and int(canvas.coords(oval)[1]) < int(canvas.coords(r_plat)[3]):
        vector_x = - vector_x
    if int(centre_coords(oval)[0] + 5) == int(centre_coords(l_plat)[0]) and int(canvas.coords(oval)[1]) > int(canvas.coords(l_plat)[1]) and int(canvas.coords(oval)[1]) < int(canvas.coords(l_plat)[3]):
        vector_x = - vector_x
root.mainloop()