import sys

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

left, right = 0, N - 1

minValue = 100000000

while left < right:
    temp = arr[left] + arr[right]

    if abs(minValue) > abs(temp):
        minValue = temp
    if temp < 0:
        left += 1
    else:
        right -= 1

print(minValue)