list = []
ip = True
buf = float(0)
max = 0
counter = 0
while ip != 0:
    counter += 1
    ip = int(input(': '))
    buf += ip
    if ip > max:
        max = ip

print(max)
print(buf/ (counter - 1))


