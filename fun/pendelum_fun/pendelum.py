from tkinter import *
main = Tk()
canvas_width = 1100
canvas_height = 1100
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.create_oval(50,50,1050,1050,width=5)
canvas.create_line(550,550,550,1050,width=5)
centre = (550,550)

class gulicka:
    def __init__(self,start,color):
        self.start = start
        self.color = color
        self.s = canvas.create_oval(start[0]-5,start[1]-5,start[0]+5,start[1]+5,outline=color)
        self.l = canvas.create_line(start[0],start[1],550,550)










canvas.pack()











mainloop()