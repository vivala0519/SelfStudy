# arr = ['las', 'god', 'psala', 'sal']
import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

while arr:
    x = arr.pop()
    if x[::-1] in arr or x == x[::-1]:
        print(len(x), x[len(x)//2])
        break