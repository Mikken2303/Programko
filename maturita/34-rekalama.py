from tkinter import *
w = 500
h = 500
canvas = Canvas(width=w, height=h,bg="white")
canvas.pack()
r = canvas.create_text(250,250, anchor=CENTER,text="ide vozik s jedolm zasunte si...")
while True:
    canvas.move(r,1,0,)
    canvas.after(1,)
    canvas.update()


canvas.mainloop()