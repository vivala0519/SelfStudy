import sys

INF = 1000000

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))
graph = [[INF] * n for _ in range(n)]
result = 0

for _ in range(r):
    a, b, l = map(int, sys.stdin.readline().split())

    graph[a - 1][b - 1] = graph[b - 1][a - 1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    temp = 0
    for j in range(n):
        if graph[i][j] <= m:
            temp += items[j]

    result = max(result, temp)

print(result)