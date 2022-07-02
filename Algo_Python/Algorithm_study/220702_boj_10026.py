import sys, copy

sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
rg = 0
r = 0
g = 0
b = 0

graph = []
for _ in range(N):
    graph.append(list(map(str, sys.stdin.readline().rstrip())))
rg_greed = copy.deepcopy(graph)

def RedGreenCompDFS(x,y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if rg_greed[x][y] == 'R' or rg_greed[x][y] == 'G':
        rg_greed[x][y] = 'visited'
        RedGreenCompDFS(x + 1, y)
        RedGreenCompDFS(x - 1, y)
        RedGreenCompDFS(x, y + 1)
        RedGreenCompDFS(x, y - 1)
        return True
    return False

def ColorDFS(x,y,color):

    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if graph[x][y] == color:
        graph[x][y] = 'visited'
        ColorDFS(x + 1, y, color)
        ColorDFS(x - 1, y, color)
        ColorDFS(x, y + 1, color)
        ColorDFS(x, y - 1, color)
        return True
    return False

for i in range(N):
    for j in range(N):
        if ColorDFS(i,j,'R') == True:
            r += 1
        if ColorDFS(i,j,'G') == True:
            g += 1
        if ColorDFS(i,j,'B') == True:
            b += 1

for i in range(N):
    for j in range(N):
        if RedGreenCompDFS(i,j) == True:
            rg += 1

print(r + g + b, rg + b)