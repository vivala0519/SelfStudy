import heapq, sys
from sys import maxsize

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
visited = [maxsize] * (N + 1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))

start, end = map(int, sys.stdin.readline().split())


def dijk(x):
    hq = []
    heapq.heappush(hq, (0, x))
    visited[x] = 0

    while hq:
        d, x = heapq.heappop(hq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                heapq.heappush(hq, (nd, nx))
                visited[nx] = nd


dijk(start)

print(visited[end])