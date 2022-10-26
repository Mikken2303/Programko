# sam neviem co som robil xd
# note to self treba prerobit + prirobit ci prospel neprosl atd
# ale ide to so shut up

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

