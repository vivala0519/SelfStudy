import sys

N = int(sys.stdin.readline())
arr = []
result = 0

for i in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

for i in range(N):
    if i % 3 != 2:
        result += arr[i]

print(result)