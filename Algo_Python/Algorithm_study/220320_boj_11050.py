import sys

N, K = list(map(int, sys.stdin.readline().rstrip().split()))

x = 1
for i in range(N, N-K, -1):
    x *= i

y = 1
for i in range(1, K+1):
    y *= i

print(x // y)