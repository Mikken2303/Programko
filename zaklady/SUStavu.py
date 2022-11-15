vstup = 53858
sus = 16
out = ""
l = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
while vstup != 0:
    out += l[vstup%sus]
    vstup = vstup // sus
print(out[::-1])




