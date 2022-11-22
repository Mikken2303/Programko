ip = "732D"
sus = 16
out = 0
c = 0
l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
## over ci su cisla dobre
for i in ip:
    if l.index(i) >= sus:
        print("zle cislice musia byt menej ako SUStava")
########
out = 0
for i in range(len(ip)):
    out = out * sus + l.index(ip[i])
print(int(ip,sus))
print(out)
