rod = "040323/3908"
den = int(rod[4:6])
mesiac = int(rod[2:4])
rok = int(rod[:2])
z = False
if int(rod[:6] + rod[7:]) % 11 == 0:
    if mesiac > 50:
        z = True
        mesiac -= 50
    if int(rod[:2]) > 21:
        plus = 1900
    else:
        plus = 2000
    print(f"narodeniny {den}. {mesiac}. {rok + plus} ")

    if z: print("zena")
    else: print("muz")
else:
    print("nie je rodne cislo")