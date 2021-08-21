s = 'c i n'
print(s)

result = '#'
arr = []
arr = s.split(' ')
arr = list(filter(None, arr))
print(arr)
for i in range(0, arr.__len__()):
    result += arr[i].capitalize()
print(result)