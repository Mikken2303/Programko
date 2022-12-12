max = 0
meno = []
for i in open("behy.txt", "r").readlines():

    if int(i.strip("\n").split(" ")[1]) > int(max):
        max = i.strip("\n").split(" ")[1]
        meno = []
        meno.append(i.strip("\n").split(" ")[0])
    elif int(i.strip("\n").split(" ")[1]) == int(max):
        meno.append(i.strip("\n").split(" ")[0])


print(max, meno)
