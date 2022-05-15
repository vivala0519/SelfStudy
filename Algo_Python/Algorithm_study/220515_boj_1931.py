import sys


N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().split())))


arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
tail = arr[0][1]
for i in range(1, N):
    if arr[i][0] >= tail:
        tail = arr[i][1]
        cnt += 1

print(cnt)