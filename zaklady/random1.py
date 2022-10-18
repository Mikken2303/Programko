from random import *
pokus, bod, counter, pocet_prik = 0,0,0, 4
while counter < pocet_prik:
    a, b = randint(0,10), randint(0,10)
    vsld = a * b
    if int(input(f"{a} * {b} = ")) == vsld: bod += 3
    elif int(input(f"chyba skus znova {a} * {b} = ")) == vsld: bod += 2
    elif int(input(f"chyba skus znova {a} * {b} = ")) == vsld: bod += 1
    else: print(f"{a} * {b} == {vsld} ")
    counter += 1
print(f"dosiahol si {bod} z {pocet_prik*3}")