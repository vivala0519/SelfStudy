m = 2
n = 4

arr = []
for i in range(m, n + 1):
    for j in range(i, n + 1):
        arr.append((i, j))
print(arr)