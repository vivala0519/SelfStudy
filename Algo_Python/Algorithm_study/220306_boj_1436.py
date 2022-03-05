# n = 6
import sys
n = int(sys.stdin.readline().rstrip())

cnt = 1
s = '666'
start = 666
while cnt < n:
    start += 1
    if s in str(start):
        cnt += 1
print(start)