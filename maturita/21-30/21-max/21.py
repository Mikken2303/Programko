def max(l):
    c = 0
    for i in l:
        if int(i) > c:
            c = int(i)
    return c
me = []
ma = []
for i in open("skok_do_dialky.txt", "r").readlines():
    me.append(i.split(' ')[0])
    t = i.strip("\n").split(' ')[1:]
    ma.append(max(t))
v = []
k = 0
for i in range(0,len(me)):
    if ma[i] > k:
        k = ma[i]
        v = []
        v.append(f"{me[i]} : {ma[i]}")
    elif ma[i] == k:
        v.append(f"{me[i]} : {ma[i]}")


print(me)
print(ma)
print(v)