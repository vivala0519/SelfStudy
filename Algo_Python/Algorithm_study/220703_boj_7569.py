from collections import deque
import sys
M, N, H = map(int, sys.stdin.readline().split())
a = [[list(map(int, sys.stdin.readline().split())) for i in range(N)] for depth in range(H)]
 
z = 1
result = -1
q = deque()
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if a[nz][nx][ny] == 0:
                    a[nz][nx][ny] = a[z][x][y] + 1
                    q.append([nz, nx, ny])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if a[i][j][k] == 1:
                q.append([i, j, k])

bfs()

for i in a:
    for j in i:
        for k in j:
            if k == 0:
                z = 0

            result = max(result, k)

if z == 0:
    print(-1)
elif result == 1:
    print(0)
else:
    print(result - 1)
