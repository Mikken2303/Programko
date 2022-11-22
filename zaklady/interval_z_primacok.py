n=100
vsetko = []
for i in range(1,n+1):
    vsetko.append(i)
x = 0
zle = []
while x + 3 < n:
    x += 3
    zle.append(x)
y = 2
while y**2 < n:
    y = y**2
    zle.append(y)
z = 5
print(z)
while z + 10 < n:
    z += 10
    print(z)
    zle.append(z)

dobre = []
for i in vsetko:
    if i in zle:
        pass
    else:
        dobre.append(i)
print(dobre)

