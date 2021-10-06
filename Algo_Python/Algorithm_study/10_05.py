value = 1652
print(len(str(value)))
length = len(str(value))
arr = []
for i in range(0, len(str(value))):
    arr.append(int(str(value)[i]))
print(arr)
total = 0
for i in range(0, arr.__len__()):
    total += arr[i] ** length
print(total)
