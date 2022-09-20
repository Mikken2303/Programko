# window moc velke zobrat pouzitie sipok a dat do toho z local

from tkinter import *
main = Tk()
canvas = Canvas()
canvas_width = 2000
canvas_height = 1000
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.pack()
ball_width = 25
ball_speed = 5
ball = canvas.create_oval(1000-ball_width/2,500-ball_width/2,1000+ball_width/2,500+ball_width/2,fill="black",width=0)
padle = canvas.create_rectangle(950,840,1050,850,fill="black",width=0)

vector = [1,1]

def center_coords(object):
    x = (canvas.coords(object)[0] + canvas.coords(object)[2]) / 2
    y = (canvas.coords(object)[1] + canvas.coords(object)[3]) / 2
    return x,y
def left(event):
    canvas.move(padle,-50,0)

def right(event):
    canvas.move(padle,50,0)

main.bind("<Left>", left)
main.bind("<Right>", right)

while True:
    print(center_coords(ball))

    if center_coords(ball)[0] < ball_width/2 or center_coords(ball)[0] > 2000-ball_width/2:
        vector[0] = -vector[0]

    if center_coords(ball)[1] < ball_width/2 or center_coords(ball)[1] > 1000-ball_width/2:
        vector[1] = -vector[1]
    if (center_coords(ball)[1] + ball_width) == 850 and center_coords(ball)[0] > (center_coords(padle)[0] - 50) and center_coords(ball)[0] < (center_coords(padle)[0] + 50):
        vector[1] = -vector[1]
    if center_coords(padle)[0] < 0:
        canvas.move(padle,1999,0)
    if center_coords(padle)[0] > 2000:
        canvas.move(padle, -1999, 0)
    canvas.create_oval(canvas.coords(ball),width=0,fill="black")
    canvas.move(ball,vector[0]*ball_speed,vector[1]*ball_speed)
    canvas.update()
    canvas.after(1)

mainloop()