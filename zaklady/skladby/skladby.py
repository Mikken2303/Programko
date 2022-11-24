s = open("skladby.txt", "r")
l = []
t = 0
for i in s.readlines():
    l.append((i.split(" ")[1].strip("\n")))
for i in l:
    t += int(i.split(":")[0])*60 + int(i.split(":")[1])
print(t)
print(f"{t//60}:{t%60}")