s = open("poznamky.txt", "w")
for i in range(1,5):
    for j in range(1,10,2):
        for k in range(7,10):
            for l in range(2,10,2):
                s.write(f"{i} {j} {k} {l} \n")
s.close()


