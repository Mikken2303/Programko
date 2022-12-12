for i in open("pracdoba.txt", "r"):
    l = i.strip("\n").split(" ")
    t1 = int(l[1].split(":")[0])*60 + int(l[1].split(":")[1])
    t2 = int(l[2].split(":")[0])*60 + int(l[2].split(":")[1])
    t = t2 - t1
    if t%60 == 0: s = "00"
    else: s = t%60
    print(f"{l[0]} {t//60}:{s}")