from random import *
pocet = 200000000
arr = 6*[0]
for i in range(0,pocet): arr[randint(0,5)] += 1
for i in range(0,6): print(f"{i} : {arr[i]}")
print(f"najcastejsie padla  {arr.index(max(arr))}")