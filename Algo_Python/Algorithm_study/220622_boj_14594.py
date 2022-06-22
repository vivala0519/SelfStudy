import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [0] * (N + 1)
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, y):
        arr[i] = 1

result = arr.count(0)
print(result - 1)