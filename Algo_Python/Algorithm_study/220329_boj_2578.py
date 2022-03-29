# pan = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
#
# ann = [[5, 10, 7, 16, 2], [4, 22, 8, 17, 13], [3, 18, 1, 6, 25], [12, 19, 23, 14, 21], [11, 24, 9, 20, 15]]
#
# check = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# print(check)

import sys

pan = []
ann = []
check = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
for _ in range(5):
    pan.append(list(map(int, sys.stdin.readline().rstrip().split())))
for _ in range(5):
    ann.append(list(map(int, sys.stdin.readline().rstrip().split())))


cnt = 0
isbreak = False
for a1 in ann:
    for a2 in a1:
        for i in range(len(pan)):
            if a2 in pan[i]:
                check[i][pan[i].index(a2)] = 1
                cnt += 1
                bingo = 0
                for k in range(len(check)):
                    if sum(check[k]) == 5:
                        bingo += 1
                    if sum([k2[k] for k2 in check]) == 5:
                        bingo += 1
                temp = 0
                tot = 0
                while temp < 5:
                    tot += check[temp][len(check)-1-temp]
                    temp += 1
                if tot == 5:
                    bingo += 1
                temp = 0
                tot = 0
                while temp < 5:
                    tot += check[temp][temp]
                    temp += 1
                if tot == 5:
                    bingo += 1

                if bingo >= 3:
                    isbreak = True
                    break
        if isbreak is True:
            break
    if isbreak is True:
        break
print(cnt)