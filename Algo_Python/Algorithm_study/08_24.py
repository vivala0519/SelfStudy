grid = [['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']]
indexes = [1, 3, 5, 8]
grid = [x for y in grid for x in y]
index_as = []
print(grid)
result = ''
for i in indexes:
    result += grid[i-1]
print(result)