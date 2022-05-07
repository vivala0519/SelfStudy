import sys

n = int(sys.stdin.readline())

cost = []

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    cost.append([temp[0], temp[1]])

cost.sort()

arr = [0] * n

for i in range(n):
    for j in range(i, n):
        profit = cost[i][0] - cost[j][1]
        if profit > 0:
            arr[i] += profit

result = [cost[i][0] for i in range(n) if arr[i] == max(arr)]
if sum(arr) == 0:
    print(0)
else:
    print(min(result))