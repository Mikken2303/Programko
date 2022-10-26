
list = []
ip = True
pocitadlo = float(0)
max = 0
counter = 0

while ip != 0:
    counter += 1
    ip = int(input(': '))
    pocitadlo += ip
    if ip > max:
        max = ip

print(f"najhorsia znamka bola {max}. ")
print(f"priemer bol {pocitadlo / (counter - 1)}")

