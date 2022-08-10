import sys
N = int(sys.stdin.readline())

arr = [[' '] * (2 * N - 1) for i in range(N)]

def making(n, x, y):
    if n == 3:
        arr[y][x] = '*'
        arr[y+1][x-1:x+2] = '* *'
        arr[y+2][x-2:x+3] = '*****'
        return
    else:
        making(n / 2, x, y)
        making(n / 2, int(x - (n / 2)), int(y + (n / 2)))
        making(n / 2, int(x + (n / 2)), int(y + (n / 2)))

making(N, N - 1, 0)

for i in arr:
    print(''.join(i))