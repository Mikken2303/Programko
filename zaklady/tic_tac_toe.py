from tkinter import *
canvas = Canvas(width=500, height=500,bg="white")
canvas.pack()
for i in range(25,500,50):
    canvas.create_line(0,i,500,i)
    canvas.create_line(i, 0, i, 500)

def kruzok(sur):
    x = round(sur.x/50)*50
    y = round(sur.y/50)*50
    canvas.create_oval(x-23,y-23,x+23,y+23)

def krizik(sur):
    x = round(sur.x / 50) * 50
    y = round(sur.y / 50) * 50
    canvas.create_line(x - 23, y - 23, x + 23, y + 23)
    canvas.create_line(x + 23, y - 23, x - 23, y + 23)
b = True


def main(s):
    global b
    if b == True:
        kruzok(s)
        b = False
    else:
        krizik(s)
        b = True

canvas.bind("<Button-1>", main)

canvas.mainloop()