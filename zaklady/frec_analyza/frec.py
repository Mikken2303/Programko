s = open("tabulka_pocetnosti.txt", "r")
string = ""
for line in s.readlines():
    string += line.strip("\n") + " "
s.close()
alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
poc = [0]*26
for i in string:
    if i.lower() in alf:
        poc[alf.index(i.lower())] += 1

print(alf)
print(poc)