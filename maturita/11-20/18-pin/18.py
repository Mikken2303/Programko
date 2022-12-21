s = open("pin.text", "w")
for i in range(0,10,2):
    for j in [2,4]:
        for k in range(1,10,2):
            for v in range(0,8):
                s.write(f"{i}, {j}, {k}, {v}\n")