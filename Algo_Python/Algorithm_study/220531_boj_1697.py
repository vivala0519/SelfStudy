from collections import deque
import sys

x = 100000

def bfs(N, K):
    q = deque()
    q.append(N)
    while q:
        temp = q.popleft()
        if temp == K:
            print(arr[temp])
            break

        for i in (temp - 1, temp + 1, temp * 2):
            if 0 <= i <= x and not arr[i]:
                arr[i] = arr[temp] + 1
                q.append(i)


N, K = map(int, sys.stdin.readline().split())
arr = [0] * (x + 1)
bfs(N, K)