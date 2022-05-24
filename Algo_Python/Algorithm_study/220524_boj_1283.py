from collections import defaultdict
import sys
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

short = [0] * N
dic = defaultdict(int)

for i in range(len(arr)):
    sp = arr[i].split()
    temp = ''
    for j in sp:
        if short[i] == 0:
            if dic[j[0].upper()] == 0:
                temp += '[' + j[0] + ']' + j[1:]
                dic[j[0].upper()] = 1
                short[i] = 1
            else:
                temp += j
            temp += ' '
        else:
            temp += j + ' '

    if short[i] == 0:
        temp = ''
        for j in range(len(arr[i])):
            x = arr[i][j].upper()
            if dic[x] == 0 and x != ' ':
                temp += '[' + arr[i][j] + ']' + arr[i][j + 1:]
                dic[x] = 1
                break
            else:
                temp += arr[i][j]
    arr[i] = temp.rstrip() 


for i in arr:
    print(i)
# for i in range(len(arr)):
#     temp = ''
#     if '[' not in arr[i]:
#         for j in range(len(arr[i])):
#             x = arr[i][j].upper()
#             if dic[x] == 0 and x != ' ':
#                 temp += '[' + arr[i][j] + ']' + arr[i][j + 1:]
#                 dic[x] = 1
#                 break
#             else:
#                 temp += arr[i][j]
#         arr[i] = temp

# for i in arr:
#     print(i)