from math import sqrt


def prv(a):

    d = 2
    while a % d != 0 and d <= sqrt(a):
        d += 1
    if a % d == 0:
        return False
    else:
        return True


i = 3
while True:
    if prv(i):
        print(i)
    i += 2