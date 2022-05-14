import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
l, r = 0, N - 1

cnt = 0
while l < r:
    if arr[l] + arr[r] == M:
        cnt += 1
        l += 1
        r -= 1
    elif arr[l] + arr[r] < M:
        l += 1
    else:
        r -= 1
print(cnt)