import sys
result = []
while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    length = len(n)
    left, right = 0, len(n)-1
    cnt = 0
    while left < right:
        if n[left] != n[right]:
            n = str(int(n) + 1)
            n = '0' * (length - len(n)) + n
            cnt += 1
            left = 0
            right = len(n) - 1
        else:
            left += 1
            right -= 1
    result.append(cnt)
for i in result:
    print(i)
