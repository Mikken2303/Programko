from tkinter import *
canvas = Canvas(width=450, height=300,bg="white")
canvas.pack()
canvas.create_rectangle(0,100,450,200,fill="blue")
canvas.create_rectangle(0,200,450,300,fill="red")
p = PhotoImage(file="output-onlinepngtools.png")
canvas.create_image(150,155, image = p,anchor="center")
canvas.mainloop()