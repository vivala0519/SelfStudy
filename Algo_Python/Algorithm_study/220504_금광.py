from re import L


n, m = 3, 4
arr = [1, 3, 3, 2, 2, 1, 4, 1, 0, 6, 4, 7]

dp = []
index = 0
for i in range(n):
    dp.append(arr[index:index + m])
    index += m

for j in range(1, m):
    for i in range(n):
        if i == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]
        if i == n - 1:
            left_down = 0
        else:
            left_down = dp[i + 1][j - 1]
        left = dp[i][j - 1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m - 1])
print(result)