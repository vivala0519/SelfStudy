import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    target_arr = deque([0 for _ in range(n)])
    target_arr[m] = 1

    cnt = 0
    while arr:
        if arr[0] == max(arr):
            x = arr.popleft()
            y = target_arr.popleft()
            cnt += 1
            if y == 1:
                break
        else:
            x = arr.popleft()
            y = target_arr.popleft()
            arr.append(x)
            target_arr.append(y)
    print(cnt)