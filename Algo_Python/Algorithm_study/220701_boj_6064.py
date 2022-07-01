import sys

def cal(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


t = int(sys.stdin.readline())
for i in range(t):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(cal(M, N, x, y))