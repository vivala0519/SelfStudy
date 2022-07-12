import sys

def dfs(i):
    global N, M
    if i == M:
        print(*temp)
        return
    for j in arr:
        if j not in temp:
            temp.append(j)
            dfs(i + 1)
            temp.pop()

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
temp = []
dfs(0)