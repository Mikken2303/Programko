from random import randint
from tkinter import *
canvas = Canvas(width=500,height=500)
canvas.pack()
l = []
l.append(randint(1,9))
for i in range(0,7):
    l.append(randint(0, 9))
l.append(randint(1,9))

for i in range(0,len(l)):
    if l[i] != 0:
        canvas.create_line(i*25+10,10,i*25+10,100,width=l[i])
    canvas.create_text(i*25+10,125,anchor=CENTER,text=l[i])
canvas.mainloop()