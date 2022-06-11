import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
left = 0
right = 0
result = 0

while left <= right and right <= len(arr):
    temp = sum(arr[left:right])
    if temp == M:
        result += 1
    if temp <= M:
        right += 1
        continue
    elif temp > M and left < right:
        left += 1
        continue
    else:
        left += 1
        right += 1
print(result)