t = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
out = ""
pos = 0
crypt = 1
sif = "Hello"
index = 0
while len(sif) < len(t):
    sif += sif
sif = sif.lower()

for i in t:
    pos = ord(sif[index]) - 65
    if 'a' <= i <= 'z':
        if chr(ord(i) + pos) <= 'z':
            out += chr(ord(i) + pos)
        else:
            out += chr(ord(i) + pos - 26)
        pos += crypt
    elif 'A' <= i <= 'Z':
        if chr(ord(i) + pos) <= 'Z':
            out += chr(ord(i) + pos)
        else:
            out += chr(ord(i) + pos - 26)
        pos += crypt
    else:
        out += i
    index += 1
print(out)
