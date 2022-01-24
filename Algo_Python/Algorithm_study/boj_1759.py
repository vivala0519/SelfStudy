import sys
from itertools import combinations
temp = sys.stdin.readline().rstrip().split(' ')
l = int(temp[0])
c = int(temp[1])
arr = sys.stdin.readline().rstrip().split(' ')
arr.sort()

comb = list(combinations(arr, l))
for i in comb:
    count = 0
    for j in i:
        if j in 'aeiou':
            count += 1
    if (count >= 1) and (count <= l - 2):
        print(''.join(i))