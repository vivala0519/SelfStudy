# arr = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]

import sys
n = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(temp)
for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt)