import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
like = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# print(like)

result = 0
for a, b, c in combinations(range(m), 3):
    temp = 0
    for i in range(n):
        temp += max(like[i][a], like[i][b], like[i][c])
    result = max(result, temp)

print(result)