# n, m = 10, 13
# g = 'BBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nBBBBBBBBWBWBW\nBBBBBBBBBWBWB\nWWWWWWWWWWBWB\nWWWWWWWWWWBWB'
# n, m = 9, 23
# g = 'BBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBB\nBBBBBBBBBBBBBBBBBBBBBBW'
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

cnt_arr = []
def cal(arr):
    for x in range(n - 7):
        for y in range(m - 7):
            start = arr[x][y]
            cnt = 0
            for i in range(8):
                for j in range(8):
                    temp = arr[x+i][y+j]
                    if temp != start and i % 2 == 0 and j % 2 == 0:
                        cnt += 1
                    elif temp == start and i % 2 == 1 and j % 2 == 0:
                        cnt += 1
                    elif temp == start and i % 2 == 0 and j % 2 == 1:
                        cnt += 1
                    elif temp != start and i % 2 == 1 and j % 2 == 1:
                        cnt += 1
            cnt_arr.append(cnt)

cal(arr)
x_y_reverse_arr = []
for i in arr[::-1]:
    x_y_reverse_arr.append(i[::-1])
cal(x_y_reverse_arr)
x_reverse_arr = []
for i in arr[::-1]:
    x_reverse_arr.append(i)
y_reverse_arr = []
cal(x_reverse_arr)
for i in arr:
    y_reverse_arr.append(i[::-1])
cal(y_reverse_arr)
print(min(cnt_arr))