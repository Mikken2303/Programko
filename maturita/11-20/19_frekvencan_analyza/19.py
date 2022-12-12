string = ""
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
v = [0]*26
for i in open("tabulka_pocetnosti.txt", "r").readlines():
    string += i.strip("\n")
for i in string:
    if i.lower() in abc:
        v[abc.index(i.lower())] += 1
print(abc)
print(v)