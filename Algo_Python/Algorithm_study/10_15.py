numbers = [26, 23, 24, 17, 23, 24, 23, 26]
numbers_set = list(set(numbers))
print(numbers_set)
arr = []
for i in numbers_set:
    if numbers.count(i) % 2 == 0:
        arr.append(i)
print(arr)
result = []
for i in numbers:
    for j in arr:
        if i == j:
            result.append(i)
print(result)