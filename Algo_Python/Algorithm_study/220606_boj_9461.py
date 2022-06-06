import sys

dp = [0 for _ in range(101)]

dp[1], dp[2], dp[3], dp[4], dp[5] = 1, 1, 1, 2, 2

for i in range(6, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

T = int(sys.stdin.readline())
for _ in range(T):
    print(dp[int(sys.stdin.readline())])