matrix = [[1, 2], [5, 3]]
n = 2
new = [[0 for col in range(matrix.__len__() + n)] for row in range(matrix.__len__() + n)]
print(new)
for i in range(0, matrix.__len__() + n):
    if i < matrix.__len__():
        for j in range(0, matrix[i].__len__() + n):
            if j < matrix.__len__():
                new[i][j] = matrix[i][j]
            else:
                new[i][j] = sum(new[i][0:j])
    else:
        for j in range(0, matrix.__len__() + n):
            print(i, j)

print(new)
