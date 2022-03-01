

# N, K = 3, 3
# S, X, Y = 2, 3, 2
# g = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
g = []
for _ in range(N):
    g.append(list(map(int, sys.stdin.readline().rstrip().split())))
S, X, Y = map(int, sys.stdin.readline().rstrip().split())
virus = []
for i in range(N):
    for j in range(N):
        if g[i][j] != 0:
            virus.append((g[i][j], i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus.sort()
q = deque(virus)
second = 0
while q:
    if second == S:
        break
    for _ in range(len(q)):
        vi, x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = vi
                q.append((vi, nx, ny))
    second += 1
print(g[X-1][Y-1])

# second = 1
# while second <= S:
#     for k in range(1, K + 1):
#         temp = []
#         for x in range(N):
#             for y in range(N):
#                 if g[x][y] == k:
#                     for i in range(4):
#                         nx = x + dx[i]
#                         ny = y + dy[i]
#                         if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                             continue
#                         if g[nx][ny] == 0 and [x, y] not in temp:
#                             g[nx][ny] = k
#                             temp.append([nx, ny])
#     second += 1
# print(g[X-1][Y-1])