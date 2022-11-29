s = open("behy.txt", "r")
lud = []
cas = []
for i in s.readlines():
    lud.append(i.strip("\n").split(" ")[0])
    cas.append(int(i.strip("\n").split(" ")[1]))
print(lud,cas)


for j in range(0, len(cas)):
    for i in range(0, len(cas) - 1):
        if cas[i + 1] < cas[i]:
            cas[i + 1], cas[i] = cas[i], cas[i + 1]
            lud[i + 1], lud[i] = lud[i], lud[i + 1]

for i in range(0, len(cas)):
    print(lud[i],cas[i])