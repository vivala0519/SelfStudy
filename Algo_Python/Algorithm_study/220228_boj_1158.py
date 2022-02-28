# N = 7
# K = 3

import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
K -= 1
arr = [n for n in range(1, N + 1)]
k = K
result = []
while arr:
    if k > len(arr):
        k %= len(arr)
    x = arr.pop(k)
    result.append(x)
    k += K
print('<'+', '.join(map(str, result))+'>')