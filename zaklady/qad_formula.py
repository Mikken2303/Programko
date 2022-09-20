from math import *
a = -5
b = 3
c = 2

def form(a,b,c):
    x1 = (-b + sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - sqrt(b**2 - 4*a*c)) / 2*a

    return x1,x2
print(form(a,b,c))