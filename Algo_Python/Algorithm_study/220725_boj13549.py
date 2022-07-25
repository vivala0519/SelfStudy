import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

visited = [-1] * 100001
queue = deque()
queue.append(N)
visited[N] = 0
while queue:
    curr = queue.popleft()
    if curr == M:
        print(visited[M])
        break
    if 0 <= curr*2 <= 100000:
        if visited[curr*2] == -1:
            visited[curr*2] = visited[curr]
            queue.appendleft(curr * 2)
    for i in [curr+1, curr-1]:
        if 0 <= i <= 100000:
            if visited[i] == -1:
                visited[i] = visited[curr] + 1
                queue.append(i)