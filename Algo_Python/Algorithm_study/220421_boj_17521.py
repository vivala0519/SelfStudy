import sys

n, W = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

coin = 0
for i in range(len(arr) - 1):
    if coin == 0:
        if arr[i] < arr[i + 1]:
            coin = W // arr[i]
            W %= arr[i]
    else:
        if arr[i] > arr[i + 1]:
            W += coin * arr[i]
            coin = 0
    if coin != 0 and i == len(arr) - 2:
        W += coin * arr[i + 1]
print(W)