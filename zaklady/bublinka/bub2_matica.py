s = open("behy.txt", "r")
l = []

for i in s.readlines():
    l.append(i.strip("\n").split(" "))
for i in range(len(l)):
    l[i][1] = int(l[i][1])

for j in range(0, len(l)):
    for i in range(0, len(l) - 1):
        if l[i + 1][1] < l[i][1]:
            l[i + 1], l[i] = l[i], l[i + 1]

for i in l:
    print(i[0], i[1])
