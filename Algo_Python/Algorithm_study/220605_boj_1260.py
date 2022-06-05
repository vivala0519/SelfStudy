import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N + 1)]

def dfs(edges, V, visited):
    visited[V] = 1
    print(V, end=' ')

    for edge in edges[V]:
        if not visited[edge]:
            dfs(edges, edge, visited)

def bfs(edges, V, visited):
    q = deque([V])
    visited[V] = 1

    while q:
        temp = q.popleft()
        print(temp, end=' ')

        for edge in edges[temp]:
            if not visited[edge]:
                q.append(edge)
                visited[edge] = 1

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    edges[x].append(y)
    edges[y].append(x)
for i in range(1, N + 1):
    edges[i].sort()

visited = [0] * (N + 1)
dfs(edges, V, visited)
print()
visited = [0] * (N + 1)
bfs(edges, V, visited)