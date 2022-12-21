out,den,mesiac = 0,1,1
months = [31,28,31,30,31,30,31,31,30,31,30,31]
if mesiac > 12 or den > months[mesiac - 1]:
    print("chyba")
else:
    out += months[mesiac-1] - den
    for i in months[mesiac-1:-1]:
        out += i
    print(out)
