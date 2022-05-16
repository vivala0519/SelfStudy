import sys

N, S = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

# arr.sort()

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] + arr[j] <= S:
            cnt += 1
    # right = len(arr) - 1
    # while i < right:
    #     if arr[i] + arr[right] <= S:
    #         result.add((i, right))
    #     right -= 1


print(cnt)