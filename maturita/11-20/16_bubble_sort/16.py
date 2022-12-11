lud = []
cas = []
for i in open("behy.txt", "r").readlines():
    lud.append(i.strip("\n").split(" ")[0])
    cas.append(i.strip("\n").split(" ")[1])
for j in range(len(cas)):
    for i in range(len(cas) - 1):
        if cas[i] > cas[i + 1]:
            cas[i], cas[i + 1] = cas[i + 1], cas[i]
            lud[i], lud[i + 1] = lud[i + 1], lud[i]
for i in range(len(cas)):
    print(f"{cas[i]} {lud[i]}")

