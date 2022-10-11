from tkinter import *
main = Tk()
canvas = Canvas()
canvas_width = 800
canvas_height = 800
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

def premiet(x,y,z):
    a = x
    b = y
    return [a, b]

trid_kocka = [[0,0,0,],[0,0,500],[0,500,0],[0,500,500,],[500,0,0,],[500,0,500],[500,500,0],[500,500,500,]]
dvad_kocka = []
for i in trid_kocka:
    dvad_kocka.append(premiet(i[0],i[1],i[2]))
print(dvad_kocka)


for i in range(1,len(dvad_kocka)):
    canvas.create_line(dvad_kocka[i],dvad_kocka[i-1])


mainloop()
