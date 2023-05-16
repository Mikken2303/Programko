inp =709
fact = []
primes = []
c = 2
b = True
while inp != 1 or b:
    p = True
    for i in primes:
        if c % i == 0:
            p = False
            break
    if p:
        primes.append(c)
        while inp % c == 0:
            fact.append(c)
            inp = inp / c
    if c > inp:
        fact.append(inp)
        b = False
    c += 1
print(fact)