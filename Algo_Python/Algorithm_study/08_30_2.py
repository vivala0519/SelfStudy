n = 4
width = (n - 1) * 2 + 1
arr = []
for i in range(0, n):
    line = []
    for j in range(0, width):
        line.append(0)
    arr.append(line)
for i in range(0, n):
    for j in range(0, width):
        arr[i][0] = 1
        arr[i][width - 1] = 1
    for j in range(1, n):
        arr[j][j] = 1
        arr[j][width - (j+1)] = 1
print(arr)
result = ''
for i in arr:
    for j in range(0, i.__len__()):
        if i[j] == 1:
            i[j] = '*'
            result += i[j]
        else:
            i[j] = ' '
            result += i[j]
    result += '\n'
print(arr)
print(result)