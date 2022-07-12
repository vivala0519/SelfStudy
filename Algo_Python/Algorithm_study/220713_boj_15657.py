import sys

def recursive(x, y):
    if x == M:
        print(*temp)
        return
    for i in range(y, N):
        temp.append(arr[i])
        recursive(x + 1, i)
        temp.pop()


N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = []
recursive(0, 0)