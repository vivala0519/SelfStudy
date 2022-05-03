import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, len(arr) - 1

result = -1
while left <= right:
    if arr[left] == left:
        result = left
        break
    else:
        left += 1
    if arr[right] == right:
        result = right
        break
    else:
        right -= 1
print(result)