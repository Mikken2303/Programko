ip = "1111"
sus = 2
out = 0
l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
g = True
for i in ip:
    if l.index(i) > sus:
        g = False
        print("zla sus")
c = 0
if g:
    for i in ip[::-1]:
        out += l.index(i)*sus**c
        c+= 1
print(out)
print(int(ip,sus))