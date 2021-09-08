numbers = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'
numbers = numbers.split(' ')
print(numbers)
arr = []
for i in numbers:
    arr.append(int(i))
print(arr)
print(max(arr))
print(min(arr))
result = str(max(arr)) + ' ' + str(min(arr))
print(result)