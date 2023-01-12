from tkinter import *
file = open("ciernobiely_obrazok_2.txt","r")
line = file.readline()
w, h = line.split()
canvas = Canvas(width=w, height=h,bg="white")
canvas.pack()
l = []
for i in file.readlines():
    l.append(i.strip("\n"))
y = 0
for i in l:
    for x in range(int(w)):
        f = "#" + 3 * i[2*x :2*x + 2]
        canvas.create_rectangle(x,y,x+1,y+1,fill=f,width = 0)
    y+=1
    canvas.update()
canvas.mainloop()