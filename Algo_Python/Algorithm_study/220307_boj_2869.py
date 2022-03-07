A, B, V = 100, 99, 1000000000
A, B, V = 5, 1, 6
A, B, V = 2, 1, 5
# snail = 0
# day = 0
# while snail < V:
#     snail += A
#     if snail >= V:
#         day += 1
#         break
#     snail -= B
#     day += 1
# print(day)

import sys
A, B, V = map(int, sys.stdin.readline().rstrip().split())

dif = A - B
temp = (V - B) / dif
if (V - B) % dif > 0:
    temp += 1
    print(int(temp))
else:

    print(int(temp))
