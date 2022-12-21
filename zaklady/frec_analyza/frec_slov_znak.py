s = open("tabulka_pocetnosti.txt", "r")
string = ""
lajna = 0
for line in s.readlines():
    string += line.strip("\n") + " "
    lajna += 1
print(lajna)
print(len(string.split(" ")))
znak = 0
for i in string:
    if i != " ":
        znak += 1
print(znak)

