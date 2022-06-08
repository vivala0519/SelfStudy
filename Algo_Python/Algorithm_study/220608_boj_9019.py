import sys
from collections import deque

char = ['D','S','L','R']

T = int(sys.stdin.readline())

def cal(x, y):
    if y == 'D':
        return (int(x) * 2) % 10000
    elif y =='S':
        return (int(x)-1) % 10000
    elif y == 'L':
        temp = x // 1000
        return x % 1000 * 10 + temp
    elif y == 'R':
        temp = x % 10
        return x // 10 + 1000 * temp

def bfs(A, B, visited):
    q = deque([[A, '']])
    visited[A] = 1
    while q:
        num, case = q.popleft()
        if num == B:
            print(case)
            break
        for i in range(4):
            temp = cal(num, char[i])
            if visited[temp] == 0:
                q.append((temp, case + char[i]))
                visited[temp] = 1

for _ in range(T):
    visited=[0 for _ in range(10000)]
    A, B = map(int,sys.stdin.readline().split())
    bfs(A, B, visited)