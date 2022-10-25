vyr = "()()()()"
c = 0

for i in vyr:
    if i == "(":
        c += 1
    elif i == ")":
        c += -1
    if c < 0:
        print("zle")
        break

