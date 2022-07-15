import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
case = sorted(set(permutations(arr, M)))

for i in case:
    for j in i:
        print(j, end=" ")
    print()