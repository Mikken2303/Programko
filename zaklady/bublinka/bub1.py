from random import *
lud = []
for i in range(0,10):
    lud.append(randint(0, 10))

for j in range(0, len(lud)):
    for i in range(0, len(lud)-1):
        if lud[i + 1] < lud[i]:
            lud[i + 1],lud[i] = lud[i], lud[i + 1]
print(lud)

