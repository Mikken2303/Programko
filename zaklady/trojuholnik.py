a = 3
b = 4
c = 5

if (a + b) > c or  (a + c) > b or (b + c) > a:
    print("existuje")
    if a == b == c:
        print("rovnostranny")
    elif a == b or a == c or b == c:
        print("rovnoramenny")
    elif (a**2 + b**2) == c**2 or  (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2:
        print("pravouhly")
else:
    print("neexistuje")