import sys

n, d = map(int, sys.stdin.readline().rstrip().split())
total = 0
for i in range(1, n + 1):
    total += str(i).count(str(d))
print(total)