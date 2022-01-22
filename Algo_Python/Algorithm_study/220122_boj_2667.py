import sys
n = int(sys.stdin.readline().rstrip())
grid = []
for i in range(n):
    temp = []
    string = sys.stdin.readline().rstrip()
    for j in range(len(string)):
        temp.append(string[j])
    grid.append(temp)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
rows, cols = len(grid), len(grid[0])
cnt = 0
result = []
for row in range(rows):
    for col in range(cols):
        if grid[row][col] != '1':
            continue
        cnt += 1
        stack = [(row, col)]
        temp = [(row, col)]
        in_cnt = 0
        while stack:
            x, y = stack.pop()
            if grid[x][y] == '1':
                in_cnt += 1
            grid[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                    continue
                temp.append((nx, ny))
                stack.append((nx, ny))
        result.append(in_cnt)
print(cnt)
result.sort()
for i in result:
    print(i)