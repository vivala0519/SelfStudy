import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, N - 1
value = float('inf')
tempL, tempR = 0, 0

while left < right:
    temp = arr[left] + arr[right]

    if abs(temp) < value:
        value = abs(temp)
        tempL, tempR = arr[left], arr[right]

    if temp == 0:
        break
    elif temp < 0:
        left += 1
    else:
        right -= 1

print(tempL, tempR)