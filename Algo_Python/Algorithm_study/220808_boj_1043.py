import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
party = []

for i in range(M):
    temp = list(map(int, sys.stdin.readline().split()))
    party.append(temp[1:])
if arr[0] == 0:
    print(M)
else:
    del arr[0]
    stack = []
    stack.extend(arr)
    visited = [0 for _ in range(N + 1)]
    for i in arr:
        visited[i] = 1
    while stack:
        i = stack.pop()
        for j in party:
            if i in j:
                for k in j:
                    if visited[k] == 0:
                        stack.append(k)
                        arr.append(k)
                        visited[k] = 1
    cnt = 0
    for i in party:
        temp = 0
        for j in arr:
            if j in i:
                temp = 1
        if temp == 0:
            cnt += 1
    print(cnt)