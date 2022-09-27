from math import sqrt
def prv(a):

    d = 2
    while a%d != 0:
        d += 1
    if d == a:
        return True
    else:
        return False
print(prv(int(input(': '))))