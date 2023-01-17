from tkinter import *
canvas = Canvas(width=750, height=500,bg="white")
canvas.pack()
vyr = "4x((38+3x)+84).(14-5x)(16+3y)(-8-3x)"
c = 0
good = True
for i in vyr:
    if i == "(":
        c += 1
    elif i == ")":
        c += -1
    if c < 0:
        print("zle zatvorky")
        good = False
        break
x = 25
y = 25
k = 0

farby =  ['red' , 'green' , 'blue' , 'cyan' , 'yellow' ,'magenta']
for i in vyr:
    if i == "(":
        canvas.create_text(x, y,text=i,fill=farby[k])
        k += 1
    elif i == ")":
        canvas.create_text(x, y,text=i,fill=farby[k])
        k += -1

    else:
        canvas.create_text(x, y,text=i)

    x += 8

canvas.mainloop()

