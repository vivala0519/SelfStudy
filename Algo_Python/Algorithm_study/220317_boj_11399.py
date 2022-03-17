# arr = [3, 1, 4, 3, 2]

import sys
n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()

total = 0
for i in range(len(arr)):
    total += sum(arr[:i + 1])
print(total)