import sys
from collections import deque

def BFS(i):
    q = deque()
    q.append([0, i])

    max_vertex = 0
    max_dist = 0

    visited.add(i)

    while q:
        now_dist, now_ver = q.popleft()

        if now_dist > max_dist:
            max_dist = now_dist
            max_ver = now_ver

        for element in graph[now_ver]:
            next_ver, next_dist = element

            if next_ver not in visited:
                q.append([now_dist + next_dist, next_ver])
                visited.add(next_ver)

    return max_dist, max_ver

V = int(sys.stdin.readline())
graph = {}

for i in range(V):
    temp = list(map(int, sys.stdin.readline().split()))[:-1]
    index = temp.pop(0)
    graph[index] = []
    while temp:
        j = temp.pop(0)
        value = temp.pop(0)

        graph[index].append([j, value])

visited = set()
a, b = BFS(1)
visited.clear()
answer, x = BFS(b)
print(answer)