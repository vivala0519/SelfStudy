import sys

def bfs():
    R, C = map(int,sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    result = 0
    q = set([(0, 0, board[0][0])])
    while q:
        x, y, arr = q.pop()
        result = max(result, len(arr))
        if result == 26:
            return 26

        for a, b in move:
            dx = x + a
            dy = y + b
            if R > dx >= 0 and C > dy >= 0 and board[dx][dy] not in arr:
                q.add((dx, dy, arr + board[dx][dy]))
    return result

print(bfs())