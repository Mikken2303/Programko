from tkinter import *
from math import *
main = Tk()
canvas = Canvas()
canvas_width = 800
canvas_height = 800
canvas = Canvas(width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

camg = [150,150,150]
focg = [50,50,50]
zoom = 1

def premiet(point,camera,focus,d):
    f1mc = focus[0] - camera[0]
    f2mc = focus[1] - camera[1]
    f3mc = focus[2] - camera[2]
    c1mp = camera[0] - point[0]
    c2mp = camera[1] - point[1]
    c3mp = camera[2] - point[2]

    sf1mc = f1mc**2
    sf2mc = f2mc**2
    sf3mc = f3mc**2

    ypart1 = ( sqrt( (sf1mc*sf3mc) + (sf2mc*sf3mc) + ((sf1mc + sf2mc)**2) ) )/(sf1mc + sf2mc)
    ypart2 = ( ( c3mp*(sf1mc + sf2mc + sf3mc ) ) / ( (f1mc*c1mp) + (f2mc*c2mp) + (f3mc*c3mp) ) ) + camera[2] - focus[2]

    y = d*ypart1*ypart2

    xpart1 = d* ((sqrt(sf1mc +sf2mc)) / f2mc)
    xpart2 = ( sf1mc +sf2mc +sf3mc)/ ((f1mc*c1mp) + (f2mc*c2mp) + (f3mc*c3mp) )
    xpart3 = (  camera[0] - point[0] + ( (f1mc*f3mc*c3mp) / (sf1mc + sf2mc) )   )
    xpart4 = -focus[0] + camera[0] - (  (f1mc*sf3mc)/ (sf1mc +sf2mc) )

    x = xpart1*((xpart2*xpart3) + xpart4)

    return [x,y]


bod1 = [100,120,150]
bod2 = [160,80,230]
pb1 = premiet(bod1,camg,focg,zoom)
pb2 = premiet(bod2,camg,focg,zoom)
print(pb1,pb2)
canvas.create_line(int(pb1[0]),int(pb1[1]),int(pb2[0]),int(pb2[1]))









canvas.create_text(575,790,text="Za rovnice ďakujeme Martinovi Ištvánovi, IV.F, 2022/2023, GJGT BB")
mainloop()
