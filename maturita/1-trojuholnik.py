
a = int(input("1. strana trojuholnika"))
b = int(input("2. strana trojuholnika"))
c = int(input("3. strana trojuholnika"))


if (a + b) > c or (a + c) > b or (b + c) > a:
    print("existuje")
    if a == b == c:
        print("rovnostranny")
    elif a == b or a == c or b == c:
        print("rovnoramenny")
    if (a**2 + b**2) == c**2 or  (a**2 + c**2) == b**2 or (b**2 + c**2) == a**2:
        print("pravouhly")

else:
    print("neexistuje")