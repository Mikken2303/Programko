ip = "832"
sus = 8
out = 0
c = 0
for i in ip[::-1]:
    out += int(i)*(sus**c)
    c += 1

print(out)