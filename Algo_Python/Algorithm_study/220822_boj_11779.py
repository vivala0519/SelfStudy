import sys
from heapq import heappop, heappush

def dijkstra(s, e, adj_list):
    INF = 1000000
    ret = None
    h = [(0, [s], s)]
    visit = [0 for _ in range(len(adj_list))]
    while h:
        dist, route, cur = heappop(h)
        if cur == e:
            ret = (str(dist), str(len(route)), ' '.join(map(str, route)))
            break
        if visit[cur]:
            continue
        visit[cur] = 1
        for adj_dist, adj in adj_list[cur]:
            heappush(h, (adj_dist + dist, route+[adj], adj))

    return ret

n, m = int(sys.stdin.readline()), int(sys.stdin.readline())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    arr[s].append((c, e))
s, e = map(int, sys.stdin.readline().split())
result = dijkstra(s, e, arr)

print('\n'.join(result))
