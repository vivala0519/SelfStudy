import sys
N = int(sys.stdin.readline().rstrip())

beehouse = 1
cnt = 1
while N > beehouse:
    beehouse += cnt * 6
    cnt += 1
print(cnt)