den = 31
mesiac = 3
months = [31,28,31,30,31,30,31,31,30,31,30,31]
out = 0
if den > months[mesiac - 1] or mesiac > 12:
    print("chyba")
else:
    out += den
    for i in months[0:mesiac-1]:
        out += i
    print(out)
