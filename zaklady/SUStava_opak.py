ip = "732"
sus = 8
out = 0
c = 0
## over ci su cisla dobre
for i in ip:
    if int(i) >= sus:
        print("zle cislice musia byt menej ako SUStava")
########
for i in ip[::-1]:
    out += int(i)*(sus**c)
    c += 1


print(int(ip,sus))
print(out)