import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = list(map(str, sys.stdin.readline().split()))
cnt = abs(100 - N)

for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        cnt = min(cnt, len(str(i)) + abs(i - N))

print(cnt)