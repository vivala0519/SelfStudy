n = 2
x = pow(n-1, 2)
first = n + x
arr = []
for i in range(0, n):
    arr.append(first + i * 2)
print(sum(arr))