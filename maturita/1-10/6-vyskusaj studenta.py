from random import *
pokus, bod, counter, pocet_prik = 0,0,0, 4
for i in range(0,pocet_prik):
    a, b = randint(0,10), randint(0,10)
    if int(input(f"{a} * {b} = ")) == a * b: bod += 3
    elif int(input(f"chyba skus znova {a} * {b} = ")) == a * b: bod += 2
    elif int(input(f"chyba skus znova {a} * {b} = ")) == a * b: bod += 1
    else: print(f"{a} * {b} == {a * b}")
print(f"dosiahol si {bod} z {pocet_prik*3}")