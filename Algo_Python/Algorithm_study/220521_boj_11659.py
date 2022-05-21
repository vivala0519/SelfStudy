import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
new = [0]
stack = []
temp = 0
for i in arr:
    temp += i
    new.append(temp)
for _ in range(M):
    stack.append(tuple(map(int, sys.stdin.readline().split())))
for i in stack:
    print(new[i[1]] - new[i[0]-1])