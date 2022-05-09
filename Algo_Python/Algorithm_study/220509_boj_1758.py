import sys

n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr.sort(reverse=True)

result = 0
for i in range(n):
    temp = arr[i] - ((i + 1) - 1)
    if temp > 0:
        result += temp
print(result)