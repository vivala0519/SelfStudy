import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    graph = [[0] * n for _ in range(2)]

    for i in range(2):
        graph[i] = list(map(int,(sys.stdin.readline().split())))

    for j in range(1, n):
        if j == 1:
            graph[0][j] += graph[1][j-1]
            graph[1][j] += graph[0][j-1]
        else:
            graph[0][j] += max(graph[1][j-1], graph[1][j-2])
            graph[1][j] += max(graph[0][j-1], graph[0][j-2])
            
    print(max(graph[0][-1], graph[1][-1]))