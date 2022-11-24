s, l = open("pracdoba.txt", "r"), []
for i in s.readlines(): l.append(i.strip("\n").split(" "))
for i in l: print(f'{i[0]} {( (int(i[2].split(":")[0]) * 60 + int(i[2].split(":")[1])) - (int(i[1].split(":")[0]) * 60 + int(i[1].split(":")[1])) )//60}:{( (int(i[2].split(":")[0]) * 60 + int(i[2].split(":")[1])) - (int(i[1].split(":")[0]) * 60 + int(i[1].split(":")[1])) )%60}')