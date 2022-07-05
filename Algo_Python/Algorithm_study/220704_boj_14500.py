import sys
N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
g = []
result = 0

for i in range(N):
    g.append([int(x) for x in sys.stdin.readline().split()])

visited = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x,y,n,c):
    global dfs_max
    if c == 4:
        if dfs_max < n:
            dfs_max = n
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx,ny,n + g[nx][ny],c + 1)
                    visited[nx][ny] = 0

def t_spin(x,y):
    temp = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < N and 0 <= nny < M:
                for h in [-1, 1]:
                    value = g[x][y]
                    if i == 0 or i == 1:
                        sny = ny + h
                        if 0 <= sny < M:
                            value += g[nx][ny]
                            value += g[nnx][nny]
                            value += g[nx][sny]
                    elif i == 2 or i == 3:
                        snx = nx + h
                        if 0 <= snx < N:
                            value += g[nx][ny]
                            value += g[nnx][nny]
                            value += g[snx][ny]
                    if temp < value:
                        temp = value
    return temp

for i in range(N):
    for j in range(M):
        dfs_max = 0
        visited[i][j] = 1
        dfs(i, j, g[i][j], 1)
        visited[i][j] = 0
        block_max = max(dfs_max, t_spin(i, j))
        result = max(result, block_max)

print(result)