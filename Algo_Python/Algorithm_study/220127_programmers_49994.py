dirs = 'LULLLLLLU'
command = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
x, y = (0, 0)
road = set()
cnt = 0

for i in dirs:
    next_x, next_y = x + command[i][0], y + command[i][1]
    if -5 <= next_x <= 5 and -5 <= next_y <= 5:
        road.add((x, y, next_x, next_y))
        road.add((next_x, next_y, x, y))
        print(road)
        x, y = next_x, next_y
print(len(road)//2)
