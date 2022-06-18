import math, sys

def cal(arr, n):
    for i in arr:
        for j in arr:
            for k in arr:
                if i + j + k == n:
                    print(i, j, k)
                    return
    print(0)

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True

def Primes(num):
    arr = []
    for i in range(2, num):
        if isPrime(i):
            arr.append(i)

    return arr

T = int(sys.stdin.readline())
N = []

for i in range(T):
    N.append(int(sys.stdin.readline()))

for item in N:
    cal(Primes(item), item)