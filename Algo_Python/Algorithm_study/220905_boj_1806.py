import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = N + 1
add = 0
left = 0
right = 0
while True:
    if add >= S:
        result = min(result, right - left)
        add -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        add += arr[right]
        right += 1

if result == N + 1:
    print(0)
else:
    print(result)