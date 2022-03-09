import sys

T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    num = 1
    cnt = 0
    while x <= y:
        if y - x <= num:
            cnt += 1
            break
        else:
            x += num
            y -= num
            cnt += 2
        if x >= y:
            break

        num += 1
    result.append(cnt)

for i in result:
    print(i)