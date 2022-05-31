import sys

N, r, c = map(int, sys.stdin.readline().split())

temp = 0

while N != 0:
    N -= 1
    size = 2 ** N

    if r < size and c < size:
        temp += 0

    elif r < size and c >= size:
        temp += size * size
        c -= size

    elif r >= size and c < size:
        temp += size * size * 2
        r -= size

    else:
        temp += size * size * 3
        r -= size
        c -= size

print(temp)