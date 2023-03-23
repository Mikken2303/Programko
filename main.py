inp = 79
sus = 16
l = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
out = ""
while inp != 0:
    out = l[inp % sus] + out
    inp = inp // sus

print(out)
