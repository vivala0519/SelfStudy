import sys

n = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

arr = []
for i in range(n):
    arr.append((x[i], y[i]))

arr.sort(key=lambda x: [x[1]])

result = 0
for i in range(n):
    result += arr[i][0] + (i * arr[i][1])

print(result)
