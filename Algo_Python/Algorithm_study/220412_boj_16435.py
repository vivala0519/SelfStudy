import sys
from collections import deque

# n, l = 3, 10
# arr = [10, 11, 13]
n, l = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
arr = deque(arr)
while True:
    if arr and arr[0] <= l:
        arr.popleft()
        l += 1
    else:
        break
print(l)