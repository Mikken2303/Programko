sr1 = int(input("nastavenie rotor 1. : "))
sr2 = int(input("nastavenie rotor 2. : "))
sr3 = int(input("nastavenie rotor 3. : "))
list1 = []
list2 = []
list3 = []


def r1(vstup):
    list = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
    global sr1
    for i in range(0, sr1):
        list.append(list[0])
        del list[0]
    global list1
    list1 = list
    return list[vstup]

def invr1(vstup):
    c = 0
    inv = []
    for x in range(0, 26):
        for i in list1:
            if i == c:
                inv.append(list1.index(i))
        c += 1
    return inv[vstup]

def r2(vstup):
    list = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
    global sr2
    for i in range(0, sr2):
        list.append(list[0])
        del list[0]
    global list2
    list2 = list
    return list[vstup]

def invr2(vstup):
    c = 0
    inv = []
    for x in range(0, 26):
        for i in list2:
            if i == c:
                inv.append(list2.index(i))
        c += 1
    return inv[vstup]

def r3(vstup):
    list = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
    global sr3
    for i in range(0, sr3):
        list.append(list[0])
        del list[0]
    global list3
    list3 = list
    return list[vstup]

def invr3(vstup):
    c = 0
    inv = []
    for x in range(0, 26):
        for i in list3:
            if i == c:
                inv.append(list3.index(i))
        c += 1
    return inv[vstup]

def reflector(vstup):
    list = [17, 3, 14, 1, 9, 13, 19, 10, 21, 4, 7, 12, 11, 5, 2, 22, 25, 0, 23, 6, 24, 8, 15, 18, 20, 16]
    return list[vstup]


#the danger zone
def otacanie(vst):
    global sr1
    global sr2
    global sr3
    if sr1 > 24:
        sr1 = 0
        sr2 += 1

    if sr2 > 24:
        sr2 = 0
        sr3 += 1

    sr1 += 1

    return (invr1(invr2(invr3(reflector(r3(r2(r1(vst))))))))

lk = input("vstup : ")
l = lk.lower()
n = []
for x in l:
    if x != " ":
        n.append(ord(x) - 97)

str =""

for i in n:
    str += chr(otacanie(i) + 97)

print(f"vystup: {str}")
input("off enter ")