import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def solution(x, y, break_wall, visited, graph):
    queue = deque()
    queue.append((x, y, break_wall))
    visited[x][y][break_wall] = 1

    while queue:
        x, y, break_wall = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][break_wall]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][break_wall] == 0:
                queue.append((nx, ny, break_wall))
                visited[nx][ny][break_wall] = visited[x][y][break_wall] + 1
            if graph[nx][ny] == 1 and break_wall == 1:
                queue.append((nx, ny, break_wall-1))
                visited[nx][ny][break_wall - 1] = visited[x][y][break_wall] + 1
    return -1

print(solution(0, 0, 1, visited, graph))