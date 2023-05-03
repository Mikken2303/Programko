from random import randint
l = []
for i in range(0,25):
    l.append(randint(0,100))


for i in range(len(l)):
    for j in range(len(l)-1-i):
        if l[j] > l[j+1]:
            l[j], l[j+ 1] = l[j+1], l[j]

print(l)