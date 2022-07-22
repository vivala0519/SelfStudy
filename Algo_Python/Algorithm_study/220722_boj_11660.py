import sys

N, M = map(int, sys.stdin.readline().split())
dp = [[0] * (N + 1)]

for _ in range(N):
    nums = [0] + list(map(int, sys.stdin.readline().split()))
    dp.append(nums)

for i in range(1, N + 1):
    for j in range(1, N):
        dp[i][j + 1] += dp[i][j]

for j in range(1, N + 1):
    for i in range(1, N):
        dp[i + 1][j] += dp[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)