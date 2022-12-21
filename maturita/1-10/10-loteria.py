from random import *
list_tipov = []
c = 0
k = 0
l = []
while c < 6:
    x = int(input('daj tip: '))
    if x > 49 or x < 1:
        print('musi byt od 1 do 49')
    elif x in list_tipov:
        print('nemozu sa opakovať')
    else:
        list_tipov.append(x)
        c += 1
while k < 6:
    y = randint(1,50)
    if y in l:
        pass
    else:
        l.append(y)
        k += 1
bod = 0
for i in list_tipov:
    if i in l:
        bod += 1

print(list_tipov)
print(l)
print(bod)


