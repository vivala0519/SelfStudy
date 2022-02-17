import sys
n = int(sys.stdin.readline().rstrip())

total = 0
while n >= 0:
    if n % 5 == 0:
        total += n // 5
        n %= 5
        break
    n -= 3
    total += 1
if n < 0:
    print(-1)
else:
    print(total)