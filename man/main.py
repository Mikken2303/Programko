from tkinter import *
canvas = Canvas(width=500,height=500,)
canvas.pack()
c = [250,250]
v = [0,1]
hlava = canvas.create_oval(c[0]- 5,c[0]- 5,c[1]+ 5,c[1]+ 5,fill="black")
bad = []
def left(bla):
    v[1],v[0] = -v[0],v[1]

    print(bla)
def right(bla):
    v[1], v[0] = v[0], -v[1]
    print(bla)

while True:
    canvas.move(hlava, v[0], v[1])
    canvas.create_oval(canvas.coords(hlava),fill="black")
    bad.append([canvas.coords(hlava)[0],canvas.coords(hlava)[1]])
    canvas.bind_all("<Left>",left)
    canvas.bind_all("<Right>",right)
    canvas.after(1,)
    canvas.update()
    if canvas.coords(hlava)[0] > 500 or canvas.coords(hlava)[1] > 500 or canvas.coords(hlava)[0] < 0 or canvas.coords(hlava)[1] < 0:
        canvas.create_text(250,250,text="game over")
        break

canvas.mainloop()