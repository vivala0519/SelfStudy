import sys

N, x = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, len(arr) - 1

left_result, right_result = [], []
while left <= right:
    if left_result and right_result:
        break
    if not left_result:
        if arr[left] != x:
            left += 1
        else:
            left_result.append(left)
    if not right_result:
        if arr[right] != x:
            right -= 1
        else:
            right_result.append(right)

if left_result and right_result:
    print(right_result[0] - left_result[0] + 1)
else:
    print(-1)