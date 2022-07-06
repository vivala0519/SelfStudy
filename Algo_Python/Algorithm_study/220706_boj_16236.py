from collections import deque
import sys

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y):
    q, visited = deque([(x, y)]), set([(x, y)])
    time = 0
    shark = 2  
    eat = 0   
    eat_flag = False  
    
    result = 0

    while q:
        size = len(q)

        q = deque(sorted(q))
        for _ in range(size):
            x, y = q.popleft()

            if g[x][y] != 0 and g[x][y] < shark:
                g[x][y] = 0
                eat += 1

                if eat == shark:
                    shark += 1
                    eat = 0               

                q, visited = deque(), set([(x, y)])
                eat_flag = True

                result = time

            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j
                if nx >= 0 and nx < N and ny >= 0 and ny < N and (nx, ny) not in visited:
                    if g[nx][ny] <= shark:
                        q.append((nx, ny))
                        visited.add((nx, ny))

            if eat_flag:
                eat_flag = False
                break

        time += 1
    return result

N = int(sys.stdin.readline())
g = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if g[i][j] == 9:
            x, y = i, j
            g[i][j] = 0

print(bfs(x, y))