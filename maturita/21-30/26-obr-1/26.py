from tkinter import *
file = open("komprimovany_obrazok_1.txt","r")
line = file.readline()
w, h = line.split()
w = int(w)
h = int(h)
canvas = Canvas(width=w, height=h,bg="white")
canvas.pack()
l = []
for i in file.readlines():
    l.append(i.strip("\n"))
l = l[1:]
for i in range(len(l)):
    l[i] = l[i].split(" ")

def color(bool):
    if bool:
        return "black"
    else:
        return "White"

for y in range(0,h-1):
    c = 0
    b = True
    print(y)
    for x in l[y]:
        canvas.create_line(c, y, c+int(x), y, fill=color(b))
        c += int(x)
        b = not b
    canvas.update()


print(l)


canvas.mainloop()
