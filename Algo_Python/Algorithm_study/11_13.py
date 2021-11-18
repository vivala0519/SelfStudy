seq = ['50', '51', '61', '53', '54', '60', '52', '62', '55', '56']
arr = []
for i in seq:
    arr.append(i[-1:])
arr.sort()
print(arr)
print(int(arr[-1]) + 1)