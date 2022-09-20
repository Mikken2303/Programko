from math import *
a = 5
b = 3
c = 2
def kvadraticka_rovnica(a, b, c):
    x1 = (-b + sqrt((b**2) - (4*a*c))) / (2*a)
    x2 = (-b - sqrt((b**2) - (4*a*c))) / (2*a)

    return x1,x2

try:
    print(kvadraticka_rovnica(a, b, c))
except:
    print("deskriminat nema")