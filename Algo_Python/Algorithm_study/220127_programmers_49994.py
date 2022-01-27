dirs = 'LULLLLLLU'
stack = [(5, 5)]
rows, cols = 11, 11
grid = []
for i in range(rows):
    line = []
    for j in range(cols):
        line.append(0)
    grid.append(line)
grid[5][5] = 1
cnt = 0

for i in dirs:
    x, y = stack.pop()
    if i == 'U':
        if y < 11:
            y += 1
    elif i == 'L':
        if x > 0:
            x -= 1
        print(x, y)
    elif i == 'R':
        if x < 11:
            x += 1
    elif i == 'D':
        if y > 0:
            y -= 1

    if grid[x][y] != 0:
        pass
    else:
        grid[x][y] = 1
        cnt += 1
    stack.append((x, y))

print(cnt)