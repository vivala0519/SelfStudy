import math, sys

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

N = input()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in arr:
    if isPrime(i):
        cnt += 1

print(cnt)