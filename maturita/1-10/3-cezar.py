text = "CEASER"
s = 4
result = ""
for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
        result += chr((ord(char) + s - 65) % 26 + 65)
    else:
        result += chr((ord(char) + s - 97) % 26 + 97)
print(result)
