n = 13
x = pow(n-1, 2)
print(n + x)
first = n + x
arr = []
for i in range(0, n):
    arr.append(first + i * 2)
print(arr)