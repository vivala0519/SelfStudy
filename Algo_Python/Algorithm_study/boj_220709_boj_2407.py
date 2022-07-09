import sys

n, m = map(int, sys.stdin.readline().split())

x, y = 1, 1
for i in range(n, n-m, -1):
    x *= i
for i in range(2, m + 1):
    y *= i

print(x // y)