import sys
memo = {1:1, 2:1}

def fibo(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo(n - 1) + fibo(n - 2)
    return memo[n]

n = int(sys.stdin.readline().rstrip())
print(fibo(n))