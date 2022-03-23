import sys

arr = []
K = int(sys.stdin.readline().rstrip())
for _ in range(K):
    n = int(sys.stdin.readline().rstrip())
    if n != 0:
        arr.append(n)
    else:
        arr.pop()

print(sum(arr))