strng = 'aeiou'
check = ['a', 'e', 'i', 'o', 'u']
arr = []
for i in range(0, len(strng)):
    if strng[i] not in check:
        arr.append(strng[i])
print(arr)
result = ''.join(arr)
print(result)