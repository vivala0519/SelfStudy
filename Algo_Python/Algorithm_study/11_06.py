a1 = 'xyaabbbccccdefww'
a2 = 'xxxxyyyyabklmopq'
arr = []
for i in range(len(a1)):
    if a1[i] not in arr:
        arr.append(a1[i])
    else:
        pass
for i in range(len(a2)):
    if a2[i] not in arr:
        arr.append(a2[i])
print(arr)
arr.sort()
print(arr)
result = ''.join(arr)
print(result)