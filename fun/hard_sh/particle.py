from __future__ import print_function, absolute_import
from PIL import ImageGrab
from tkinter import *
import numpy as np
import os
import time
import random

class particule:
    def __init__(self,):
        self.x=0
        self.y=0
        self.f=(0,0)
        self.a=(0,0)
        self.m=1.
        self.cv=None
    def gen(self,width, height,zmin,zmax,amin,amax,mmin,mmax):
        self.x=random.randint(0,width)
        self.y =random.randint(0,height)
        self.f=(random.uniform(-zmax,zmax), random.uniform(-zmax,zmax))
        self.a = (random.uniform(amin,amax), random.uniform(amin,amax))
        self.m=random.uniform(mmin,mmax)
        self.color= '#%02x%02x%02x' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))

class MyApp(Tk):
    def __init__(self):
        self.nbi=0
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas  = Canvas(fr, height = 728, width = 1288,bg= 'black')
        self.canvas.pack()
        nb_particules = 1000
        self.zmin=1.
        self.zmax=1.
        self.amin=0.
        self.amax=0.
        self.mmin=1
        self.mmax=10.
        self.size=3.
        self.A = (self.canvas.winfo_reqwidth()/2,self.canvas.winfo_reqheight()/2)
        self.M=50
        self.particules = list(range(nb_particules))
        for idx, p_ in enumerate(self.particules):
            self.particules[idx]=particule()
            self.particules[idx].gen(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(),self.zmin,self.zmax,self.amin,self.amax,self.mmin,self.mmax)
            self.particules[idx].cv =self.canvas.create_oval(self.particules[idx].x-self.particules[idx].m, self.particules[idx].y-self.particules[idx].m, self.particules[idx].x+self.particules[idx].m, self.particules[idx].y+self.particules[idx].m)
            self.canvas.itemconfig(self.particules[idx].cv, fill=self.particules[idx].color) # change color
        self.update_drops()


        self.canvas.bind("<Button-1>", self.click )


        return
    def click(self, event):
        print( (event.x, event.y))
        self.A=(event.x, event.y)

    def update_drops(self ):

        for idx, p_ in enumerate(self.particules):
            dx=  (self.A[0] - self.particules[idx].x)
            dy= (self.A[1]  -self.particules[idx].y)
            if np.abs(dx<100):
                dx=  np.sign(dx) *100
            if np.abs(dy<100):
                dy= np.sign(dy) *100
            d = ((dx)**2 + (dy)**2)**0.5

            f = (self.M * self.particules[idx].m) / (d**2) *1.

            dx/=d
            dy/=d
            self.particules[idx].a=(f*dx,f*dy)

            self.particules[idx].f=(self.particules[idx].f[0]+self.particules[idx].a[0],self.particules[idx].f[1]+self.particules[idx].a[1])

            self.particules[idx].x +=  self.particules[idx].f[0]
            self.particules[idx].y +=  self.particules[idx].f[1]
            self.canvas.coords(self.particules[idx].cv,self.particules[idx].x-self.particules[idx].m, self.particules[idx].y-self.particules[idx].m, self.particules[idx].x+self.particules[idx].m, self.particules[idx].y+self.particules[idx].m)

        self.canvas.update()

        return
if __name__ == "__main__":
    root = MyApp()
    i=0
    while 1:
        root.update_drops( )
        root.after(1)
