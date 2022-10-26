from random import *
tip,hod = [8,11,42,34,44,45],[]
for i in range(0,6): hod.append(randint(1,99))
body = 0
for i in tip:
    if i in hod: body += 1
print(tip,hod,body)