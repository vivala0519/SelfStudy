import sys
from itertools import combinations_with_replacement

N = int(sys.stdin.readline())

roadToRoma = [1, 5, 10, 50]
arr = set()

for i in combinations_with_replacement(roadToRoma, N):
    arr.add(sum(list(i)))

print(len(arr))