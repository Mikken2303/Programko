vstup = 538
sus = 8
out = ""
while vstup != 0:
    out += str(vstup%sus)
    vstup = vstup // sus
print(out[::-1])




