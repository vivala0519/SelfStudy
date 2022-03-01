import sys

N = int(sys.stdin.readline().rstrip())
pattern = sys.stdin.readline().rstrip()
arr = [sys.stdin.readline().rstrip() for n in range(N)]
x, y = pattern.split('*')
for i in arr:
    if x == i[:len(x)] and y == i[-len(y):] and len(x+y) <= len(i):
        print('DA')
    else:
        print('NE')