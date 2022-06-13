from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):

    def bfs(idx, graph, visited):
        q = deque()
        q.append(idx)
        visited[idx] = 1
        cnt = 0
        while q:
            temp = q.popleft()
            for i in graph[temp]:
                if not visited[i]:
                    visited[i] = 1
                    cnt += 1
                    q.append(i)
        return cnt

    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())

        graph[x].append(y)
        graph[y].append(x)
    
    visited = [0 for _ in range(N + 1)]

    print(bfs(1, graph, visited))
