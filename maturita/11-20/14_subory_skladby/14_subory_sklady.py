out = 0
for i in open("skladby.txt", "r").readlines():
    out += int(i.split(" ")[1].strip("\n").split(":")[0])*60 + int(i.split(" ")[1].strip("\n").split(":")[1])
print(f"{out//60}:{out%60}")

