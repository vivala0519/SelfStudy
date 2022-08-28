import sys

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x


N, M = map(int, sys.stdin.readline().split())
parent = list(range(N + 1))
edges = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])

cost, lastChild = 0, 0

for v1, v2, c in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        cost += c
        lastChild = c

print(cost - lastChild)