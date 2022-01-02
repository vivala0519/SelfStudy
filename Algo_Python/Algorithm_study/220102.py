data = 'iiisdoso'
num = 0
arr = []
for i in range(len(data)):
    if data[i] == 'i':
        num += 1
    elif data[i] == 'd':
        num -= 1
    elif data[i] == 's':
        num = pow(num, 2)
    elif data[i] == 'o':
        arr.append(num)
    else:
        pass
print(arr)