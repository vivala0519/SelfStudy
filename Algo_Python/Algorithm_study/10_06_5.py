arr = [1, 2, 3, 4, 5]

temp = []
for k in range(1, arr.__len__() + 1):
    for i in range(0, arr.__len__()):
        # print(arr[i:i+2])
        count = 0
        for j in range(0, arr[i:i+k].__len__()):
            if arr[i:i+k][j] % 2 != 0:
                count += 1
        if count % 2 != 0:
            if arr[i:i+k] in temp:
                pass
            else:
                temp.append(arr[i:i+k])

print(temp)
# temp = list(set(list(map(tuple, temp))))
# print(len(temp))

