array = [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]
arr = []
for i in array:
    if not i:
        print(i)
    else:
        for j in i:
            arr.append(j)
print(arr)
arr.sort()
print(arr)