ip = "732F"
sus = 16
out = 0
c = 0
l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
## over ci su cisla dobre
k = True
for i in ip:
    if i in l[:sus]:
        pass
    else:
        print("zle cislice musia byt menej ako SUStava")
        k = False

if k:
    for i in ip[::-1]:
        out += l.index(i)*(sus**c)
        c += 1
print(int(ip, sus))
print(out)