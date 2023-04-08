s = open("pracdoba.txt","r")
l = []
for i in s.readlines():
    l.append(i.strip("\n").split(" "))

for i in l:
    print(i)
    c1 = int(i[1].split(":")[0]) * 60 + int(i[1].split(":")[1])
    c2 = int(i[2].split(":")[0]) * 60 + int(i[2].split(":")[1])
    t = c2 - c1
    if t%60 == 0:
        m="00"
    else:
        m=t%60
    print(f"{i[0]} {t//60}:{m}")
