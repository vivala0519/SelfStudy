import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = {i: i for i in range(1, 101)}
for _ in range(N + M):
    a, b = map(int, sys.stdin.readline().split())
    board[a] = b

q = deque([(1, 0)])
visited = [False] * 101
visited[1] = True
while q:
    now, count = q.popleft()
    if now == 100:
        print(count)
        break
    for i in range(1, 7):
        if board.get(now + i) is not None and not visited[board[now + i]]:
            q.append((board[now + i], count + 1))
            visited[board[now + i]] = True