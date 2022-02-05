n = 7
arr = [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]

import sys
n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
arr.sort()

total = 0
maxH = 0
maxL = arr[len(arr)-1][0]
for i in arr:
    if i[1] > maxH:
        maxH = i[1]
        maxidx = i[0]

height_list = [0] * (maxL + 1)
for i in arr:
    height_list[i[0]] = i[1]
# print(height_list)
now = 0
for i in range(maxidx + 1):
    if height_list[i] > now:
        now = height_list[i]
    total += now
# print(total)
for i in range(maxL, maxidx, -1):
    temp = height_list[maxL]
    if height_list[i] > temp:
        temp = height_list[i]
    total += temp
print(total)