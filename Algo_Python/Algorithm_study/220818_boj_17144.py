import sys

R, C, T = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

def spread():
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    sp = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            if graph[x][y] == 0 or graph[x][y] == -1:
                continue

            dust = graph[x][y] // 5

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                    sp[nx][ny] += dust
                    sp[x][y] -= dust

    for i in range(R):
        for j in range(C):
            graph[i][j] += sp[i][j]


def topFunc():
    dx, dy = (0, -1, 0, 1), (1, 0, -1, 0)
    x, y, d = top, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == top and y == 0:
            break
        if not 0 <= nx < R or not 0 <= ny < C:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


def bottomFunc():
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    x, y, d = bottom, 1, 0
    prev = 0

    while True:
        nx, ny = x + dx[d], y + dy[d]

        if x == bottom and y == 0:
            break
        if not 0 <= nx < R or not 0 <= ny < C:
            d += 1
            continue

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny

for i in range(R):
    if graph[i][0] == -1:
        top = i
        bottom = i + 1
        break

for _ in range(T):
    spread()
    topFunc()
    bottomFunc()

print(sum(map(sum, graph)) + 2)