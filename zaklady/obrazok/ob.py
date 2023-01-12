from tkinter import *
file = open("ciernobiely_obrazok_2.txt","r")
line = file.readline()
w, h = line.split()
canvas = Canvas(width=w, height=h,bg="white")
l = []
for i in file.readlines():
    l.append(i.strip("\n"))

print(l)