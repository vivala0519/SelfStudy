# x1, y1, r1, x2, y2, r2 = 0, 0, 13, 40, 0, 37
import math, sys

result = []
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    dif = math.sqrt((x1-x2) ** 2 + (y1 - y2) ** 2)

    temp = [dif, r1, r2]
    x = max(dif, r1, r2)
    temp.remove(x)
    if dif == 0 and r1 == r2:
        result.append(-1)
    elif dif == r1 + r2 or abs(r1-r2) == dif:
        result.append(1)
    elif abs(r1-r2) < dif < (r1+r2):
        result.append(2)
    else:
        result.append(0)
for i in result:
    print(i)