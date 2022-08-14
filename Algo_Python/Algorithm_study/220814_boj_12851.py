import sys
from collections import deque


def BFS(su):
    q = deque([])
    q.append(su)
    board[su][0] = 0
    board[su][1] = 1
    while q:
        x = q.popleft()
        for nx in [x + 1, x - 1, x * 2]:
            if 0 <= nx <= 100000:
                if board[nx][0] == -1:
                    board[nx][0] = board[x][0]+1
                    board[nx][1] = board[x][1]
                    q.append(nx)
                elif board[nx][0] == board[x][0]+1:
                    board[nx][1] += board[x][1]

N, K = map(int, sys.stdin.readline().split())
board = [[-1, 0] for _ in range(100001)]

BFS(N)
print(board[K][0])
print(board[K][1])