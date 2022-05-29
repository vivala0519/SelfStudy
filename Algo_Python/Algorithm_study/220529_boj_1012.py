import sys
from collections import deque

T = int(sys.stdin.readline())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(g, a, b):
    q = deque()
    q.append((a, b))
    g[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if g[nx][ny] == 1:
                g[nx][ny] = 0
                q.append((nx, ny))
    return

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    g = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        g[x][y] = 1

    for i in range(N):
        for j in range(M):
            if g[i][j] == 1:
                bfs(g, i, j)
                cnt += 1
    print(cnt)