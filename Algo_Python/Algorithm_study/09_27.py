sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
for i in range(0, sizes.__len__()):
    if sizes[i][0] < sizes[i][1]:
        temp = sizes[i][0]
        sizes[i][0] = sizes[i][1]
        sizes[i][1] = temp
ver = []
hor = []
for i in range(0, sizes.__len__()):
    ver.append(sizes[i][0])
    hor.append(sizes[i][1])
print(ver)
width = max(ver)
height = max(hor)
print(width, height)
result = max(ver) * max(hor)
print(result)