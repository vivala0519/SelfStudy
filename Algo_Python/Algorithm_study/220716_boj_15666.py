import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
arr = set(map(int, sys.stdin.readline().split()))
temp = combinations_with_replacement(sorted(arr), M)

for i in temp:
    for j in i:
        print(j, end=" ")
    print()