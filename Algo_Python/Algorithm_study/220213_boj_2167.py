# n, m = 2, 3
# arr = [[1, 2, 4], [8, 16, 32]]
# i, j, x, y = 1, 3, 2, 3
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
k = int(sys.stdin.readline().rstrip())
result_arr = []

def cal(i, j, x, y):
    result = 0
    for a in range(i-1, x):
        for b in range(j - 1, y):
            result += arr[a][b]
    result_arr.append(result)

for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().rstrip().split())
    cal(i, j, x, y)

for i in result_arr:
    print(i)