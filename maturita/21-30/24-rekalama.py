from tkinter import *
w = 500
h = 500
canvas = Canvas(width=w, height=h,bg="white")
canvas.pack()
r1 = canvas.create_text(0,250, anchor=CENTER,text=" ide vozik s jedlom zasunte si..")
r2 = canvas.create_text(600,250, anchor=CENTER,text=" ide vozik s jedlom zasunte si..")
while True:
    canvas.move(r1,2,0,)
    canvas.move(r2, 2, 0, )
    if canvas.coords(r1)[0] > 900:
        canvas.move(r1, -1025,0)
    if canvas.coords(r2)[0] > 900:
        canvas.move(r2, -1025,0)
    canvas.after(1,)
    canvas.update()


canvas.mainloop()