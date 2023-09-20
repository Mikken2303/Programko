from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500)
canvas.pack()
radius = 10

oval = canvas.create_oval(300,200,310,210, fill=("black"))
x = 1
y = 1
plat = canvas.create_line(200,400,300,400,width="5")
block1 = canvas.create_line(0,100,100,100,width="25")
block2 = canvas.create_line(100,100,200,100,width="25")
block3 = canvas.create_line(200,100,300,100,width="25")
block4 = canvas.create_line(300,100,400,100,width="25")
block5 = canvas.create_line(400,100,500,100,width="25")

block11 = canvas.create_line(0,75,100,75,width="25")
block12 = canvas.create_line(100,75,200,75,width="25")
block13 = canvas.create_line(200,75,300,75,width="25")
block14 = canvas.create_line(300,75,400,75,width="25")
block15 = canvas.create_line(400,75,500,75,width="25")

line = canvas.create_line(0,0,0,0)
b1,b2,b3,b4,b5 = True,True,True,True,True
b11,b12,b13,b14,b15 = True,True,True,True,True


def lavo(sur):
   canvas.move(plat,-25,0)
   sur = 0
def pravo(sur):
   canvas.move(plat,25,0)
   sur = 0

zivoty = 3
ziv1 = canvas.create_oval(10,10,20,20, fill="red")
ziv2 = canvas.create_oval(25,10,35,20, fill="red")
ziv3 = canvas.create_oval(40,10,50,20, fill="red")

while True:

    root.bind("<Left>", lavo)
    root.bind("<Right>", pravo)
    canvas.move(oval, x,y)
    canvas.after(1,)
    canvas.update()
    canvas.delete(line)
    #line = canvas.create_line(((canvas.coords(oval)[0] + canvas.coords(oval)[2]) / 2),((canvas.coords(oval)[1] + canvas.coords(oval)[3]) / 2),1000*x,1000*y)

    if canvas.coords(oval)[0] > 500 or canvas.coords(oval)[0] < 0:
        x = -x
    if canvas.coords(oval)[1] > 500:
        y = -y
        zivoty += -1
    if canvas.coords(oval)[1] < 0 :
        y = -y
    if int(canvas.coords(oval)[1]) == 390 and int(canvas.coords(oval)[0]) > int(canvas.coords(plat)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(plat)[2]):
        y = -y

    if canvas.coords(plat)[0] > 500:
        canvas.move(plat,-600,0)
    if canvas.coords(plat)[2] < 0:
        canvas.move(plat,600,0)

    if b1 and int(canvas.coords(oval)[1]) == 110 and int(canvas.coords(oval)[0]) > int(canvas.coords(block1)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block1)[2]):
            y = -y
            canvas.delete(block1)
            b1 = False
    if b2 and int(canvas.coords(oval)[1]) == 110 and int(canvas.coords(oval)[0]) > int(canvas.coords(block2)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block2)[2]):
            y = -y
            canvas.delete(block2)
            b2 = False
    if b3 and int(canvas.coords(oval)[1]) == 110 and int(canvas.coords(oval)[0]) > int(canvas.coords(block3)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block3)[2]):
            y = -y
            canvas.delete(block3)
            b3 = False
    if b4 and int(canvas.coords(oval)[1]) == 110 and int(canvas.coords(oval)[0]) > int(canvas.coords(block4)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block4)[2]):
            y = -y
            canvas.delete(block4)
            b4 = False
    if b5 and int(canvas.coords(oval)[1]) == 110 and int(canvas.coords(oval)[0]) > int(canvas.coords(block5)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block5)[2]):
            y = -y
            canvas.delete(block5)
            b5 = False

    if b11 and int(canvas.coords(oval)[1]) == 85 and int(canvas.coords(oval)[0]) > int(canvas.coords(block11)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block11)[2]):
        y = -y
        canvas.delete(block11)
        b11 = False
    if b12 and int(canvas.coords(oval)[1]) == 85 and int(canvas.coords(oval)[0]) > int(canvas.coords(block12)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block12)[2]):
        y = -y
        canvas.delete(block12)
        b12 = False
    if b13 and int(canvas.coords(oval)[1]) == 85 and int(canvas.coords(oval)[0]) > int(canvas.coords(block13)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block13)[2]):
        y = -y
        canvas.delete(block13)
        b13 = False
    if b14 and int(canvas.coords(oval)[1]) == 85 and int(canvas.coords(oval)[0]) > int(canvas.coords(block14)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block14)[2]):
        y = -y
        canvas.delete(block14)
        b14 = False
    if b15 and int(canvas.coords(oval)[1]) == 85 and int(canvas.coords(oval)[0]) > int(canvas.coords(block15)[0]) and int(canvas.coords(oval)[0]) < int(canvas.coords(block15)[2]):
        y = -y
        canvas.delete(block15)
        b15 = False



    if zivoty == 2:
        canvas.delete(ziv3)
    if zivoty == 1:
        canvas.delete(ziv2)
    if zivoty == 0:
        canvas.delete(ziv1)
        canvas.create_text(250,250,text="GAME OVER",anchor = "center", font=('Helvetica', '36'))
        break
root.mainloop()