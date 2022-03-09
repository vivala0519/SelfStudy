import math, sys

def isPrime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False

    return True

temp = list(range(2, 246912))
temp_p = []
for i in temp:
    if isPrime(i):
        temp_p.append(i)
result = []
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    cnt = 0
    for i in temp_p:
        if n < i <= n*2:
            cnt += 1
    result.append(cnt)
for i in result:
    print(i)