import statistics
import math
arr = [1,52,125,10,25,201,244,192,128,23,203,98,154,255]
arr_2 = [0, 0, 255, 255, 0, 0, 255, 255, 255]
arr_3 = [100, 50, 100, 200]
# num = math.trunc(statistics.median(arr))
# print(math.trunc(statistics.median(arr)))
dis = []
trans = []
for i in range(0, arr.__len__()):
    trans.append(arr[i]+1)
print(trans)
for i in range(0, trans.__len__()):
    over = 0
    less = 0
    num = trans[i]
    for j in range(0, arr.__len__()):
        if arr[j] >= num:
            over += 1
        else:
            less += 1
    print(over, less)
    dis.append(abs(over - less))
print(dis)
temp = min(dis)
print('최소값:', temp)
mins = [i for i, ele in enumerate(dis) if ele == temp]
print(mins)
again = []
for i in mins:
    again.append(trans[i])
answer = min(again)