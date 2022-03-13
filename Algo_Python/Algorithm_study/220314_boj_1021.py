# n, m = 10, 3
# n, m = 32, 6
# n, m = 10, 10
# arr = [1, 2, 3]
# arr = [2, 9, 5]
# arr = [27, 16, 30, 11, 6, 23]
# arr = [1, 6, 3, 2, 7, 9, 8, 4, 10, 5]
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
q = deque([n for n in range(1, n + 1)])

cnt = 0
for i in arr:
    # print('for', i)
    if q.index(i) <= len(q)//2:
        while q[0] != i:
            q.append(q.popleft())
            cnt += 1
        q.popleft()
        # print(q, cnt)
    else:
        while q[0] != i:
            q.appendleft(q.pop())
            cnt += 1
        q.popleft()
        # print(q, cnt)
print(cnt)