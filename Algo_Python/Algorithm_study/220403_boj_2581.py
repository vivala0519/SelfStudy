import math, sys

arr = []
def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    arr.append(num)

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

# arr = []
for i in range(M, N + 1):
    isPrime(i)
        # arr.append(i)

if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))