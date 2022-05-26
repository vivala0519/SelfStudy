import sys
from collections import defaultdict

# arr = [6, 3, 2, 10, -10]
# get = [10, 9, -5, 2, 3, 4, 5, -10]
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
get = list(map(int, sys.stdin.readline().split()))

dic = defaultdict(int)
for i in arr:
    dic[i] = 1

result = []
for i in get:
    if dic[i] == 1:
        result.append(1)
    else:
        result.append(0)
print(' '.join(map(str, result)))