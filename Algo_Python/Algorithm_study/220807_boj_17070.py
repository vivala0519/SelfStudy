import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, N):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]

for i in range(1, N):
    for j in range(2, N):

        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))

        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[k][-1][-1] for k in range(3)))