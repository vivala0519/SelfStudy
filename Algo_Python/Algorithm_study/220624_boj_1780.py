import sys

n = int(sys.stdin.readline())
square = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
a, b, c = 0, 0, 0


def dac(data, x, y, size):
    first_node = data[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if data[i][j] != first_node:
                break
        else:
            continue
        break

    else:
        global a, b, c
        if first_node == -1:
            a += 1
        elif first_node == 0:
            b += 1
        else:
            c += 1
        return

    div = size // 3
    for i in range(3):
        for j in range(3):
            dac(data, x + i * div, y + j * div, div)


dac(square, 0, 0, n)
print(a, b, c, sep="\n")