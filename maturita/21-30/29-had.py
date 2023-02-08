from tkinter import *
w = 500
h = 500
canvas = Canvas(width=w, height=h,bg="white")
canvas.pack()
bad = []
for i in range(0,500):
    bad.append([0,i])
    bad.append([i, 0])
    bad.append([500, i])
    bad.append([i, 500])
v = [0,-1]

p = [250,250]
hlv = canvas.create_oval(250-5,250-5,250+5,250+5,fill="black")
def lv(s):
    global v
    v[0], v[1] = v[1], v[0]*-1
    print(s)
def pv(s):
    global v
    v[0], v[1] = v[1]*-1, v[0]
    print(s)
canvas.bind_all("<Left>", lv)
canvas.bind_all("<Right>", pv)

while True:
    #bad.append(p)
    canvas.create_oval(p[0]-1,p[1]-1,p[0]+1,p[1]+1)
    canvas.move(hlv,v[0],v[1])
    p[0] += v[0]
    p[1] += v[1]
    canvas.after(1)
    canvas.update()
    if p in bad:
        print("havaria")
        break

    print("c")
canvas.mainloop()