from collections import deque
import sys

N = int(sys.stdin.readline())
arr = deque(map(int, sys.stdin.readline().split()))

i = 1
result = deque([])
while arr:
    x = arr.pop()
    if x == 1:
        result.appendleft(i)
    elif x == 2:
        result.insert(1, i)
    else:
        result.append(i)
    i += 1
print(' '.join(str(x) for x in result))