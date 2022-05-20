import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


cnt = 0
for i in range(N):
    left = i
    right = N
    while left < right:
        mid = (left + right) // 2
        if arr[i] >= arr[mid] * 0.9:
            left = mid + 1
        else:
            right = mid
    cnt += right - i - 1
print(cnt)
