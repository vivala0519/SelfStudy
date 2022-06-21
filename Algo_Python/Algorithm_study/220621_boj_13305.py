import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

result = 0
temp = cost[0]
for i in range(N - 1):
    if temp > cost[i]:
        temp = cost[i]
    result += temp * road[i]

print(result)