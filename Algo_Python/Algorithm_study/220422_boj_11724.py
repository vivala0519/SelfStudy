import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

def dfs(v):
    visited[v] = True
    for i in adj[v]:
        if not visited[i]:
            dfs(i)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)