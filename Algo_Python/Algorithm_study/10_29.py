num = 231
print(str(num))
arr = []
for i in range(0, len(str(num))):
    arr.append(str(num)[i])
arr.sort()
arr.reverse()
print(arr)
result = int(''.join(arr))
print(result)
if num <= 0 or len(str(num)) != 3:
    print('None')