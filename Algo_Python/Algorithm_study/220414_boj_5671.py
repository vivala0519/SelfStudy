import sys


while True:
    read = sys.stdin.readline().rstrip()
    if not read:
        break
    N, M = map(int, read.split())

    cnt = 0
    for i in range(N, M+1):
        temp = set()
        for el in str(i):
            temp.add(el)
        if len(str(i)) == len(temp):
            cnt += 1
    print(cnt)