import sys
from collections import deque


def bfs():
    q = deque()
    q.append((0, 0))
    visit = set()
    visit.add((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visit:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
                    visit.add((nx, ny))
                else:
                    arr[nx][ny] += 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))
time = 0

while True:
    total = 0
    for i in range(N):
        total += sum(arr[i])
    if total == 0:
        print(time)
        break
    bfs()
    time += 1