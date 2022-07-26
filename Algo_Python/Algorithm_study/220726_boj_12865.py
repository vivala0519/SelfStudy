import sys

N, K = map(int, sys.stdin.readline().split())
items = []

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    items.append((a, b))

dp = [0 for _ in range(K + 1)]

for item in items:
    a, b = item
    for i in range(K, a - 1, -1):
        dp[i] = max(dp[i], dp[i - a] + b)

print(dp[-1])