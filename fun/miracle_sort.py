arr = [8,6,9,18,28,45,861]
sorted = False
while not sorted:
    sorted = True
    for i in range(0, len(arr)):
        if arr[i] < arr[i + 1]:
            sorted = False
            break
    print("getting there")

print("done")
print(arr)