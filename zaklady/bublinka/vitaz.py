s = open("behy.txt", "r")
l = []
v = []
for i in s.readlines():
    l.append(i.strip("\n").split(" "))
for i in range(len(l)):
    l[i][1] = int(l[i][1])
min = 1000

for i in l:
    if i[1] == min:
        v.append(i)
    elif i[1] < min:
        min = i[1]
        v = []
        v.append(i)
print(v)

