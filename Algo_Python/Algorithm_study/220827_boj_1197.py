import sys

def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])

    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


V, E = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2])
parent = [i for i in range(V + 1)]
answer = 0

for A, B, C in graph:
    if find(A) != find(B):
        union(A, B)
        answer += C

print(answer)