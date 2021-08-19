string = 'aba'
print(string.count('a'))

arr = []
for i in range(0, len(string)):
    arr.append(string[i])
list = []
for i in arr:
    if i not in list:
        list.append(i)
result = {}
for i in list:
    result[i] = string.count(i)
print(result)