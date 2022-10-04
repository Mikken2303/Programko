t = ""
out = ""
pos = 3
for i in t:
    if 123 > ord(i) > 96:
        if (ord(i) + pos) < 123:
            out += chr(ord(i) + pos)
        else:
            out += chr(ord(i) + pos - 26)
    elif 91 > ord(i) > 64:
        if (ord(i) + pos) < 64:
            out += chr(ord(i) + pos)
        else:
            out += chr(ord(i) + pos - 26)
    else:
        out += i

print(out)