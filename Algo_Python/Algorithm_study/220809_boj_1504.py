import sys
from heapq import heappop, heappush

maxCost = float('inf')

N, E = map(int, sys.stdin.readline().split())
G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(E):
    u, v, c = map(int, sys.stdin.readline().split())
    G[u][v] = c
    G[v][u] = c
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    heap = []
    heappush(heap, [0, start])

    visited = [-1 for _ in range(N + 1)]
    dist = [maxCost for _ in range(N + 1)]
    dist[start] = 0
    while heap:
        cost, node = heappop(heap)

        if visited[node] != 1:
            visited[node] = 1

            for next in range(1, N + 1):
                if node != next and visited[next] == -1 and G[node][next] != 0:

                    if dist[next] >= G[node][next] + cost:
                        dist[next] = G[node][next] + cost
                        heappush(heap, [dist[next], next])

    return dist


dist_start, dist_v1, dist_v2 = dijkstra(1), dijkstra(v1), dijkstra(v2)

tmp1 = dist_start[v1] + dist_v1[v2] + dist_v2[N]
tmp2 = dist_start[v2] + dist_v2[v1] + dist_v1[N]

if tmp1 == maxCost and tmp2 == maxCost:
    print(-1)
else:
    print(min(tmp1, tmp2))