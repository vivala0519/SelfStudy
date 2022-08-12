import sys

N, B = map(int, sys.stdin.readline().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def multi(a, b):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for z in range(N):
                temp[i][j] += a[i][z] * b[z][j] % 1000
    return temp

def power(a, b):
    if b == 1:
        return a
    else:
        temp = power(a, b // 2)
        if b % 2 == 0:
            return multi(temp, temp)
        else:
            return multi(multi(temp, temp), a)

result = power(matrix, B)

for row in result:
    for col in row:
        print(col % 1000, end=" ")
    print()