n = 4
k = 1
for i in range(1, n + 1):
    arr = []
    for j in range(1, i * 2):
        arr.append(k)
        k += 2
    print(arr)
    print(sum(arr[-3:len(arr)]))