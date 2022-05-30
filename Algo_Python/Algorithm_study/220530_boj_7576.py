from collections import deque
import sys


M, N = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for i in range(N):
    for j in range(M):
        if g[i][j] == 1:
            q.append([i, j])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < N and 0 <= ny < M and g[nx][ny] == 0:
            g[nx][ny] = g[x][y] + 1
            q.append([nx, ny])

temp = False
for i in g:
    for j in i:
        if j == 0:
            temp = True
            break
    result = max(result, max(i))

if temp:
    print(-1)
else:
    print(result - 1)