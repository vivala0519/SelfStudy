import sys

def sol(init, n):
    if n == 0:
        return init
    elif n == 1:
        return init
    else:
        tmp = sol(init, n//2)
        if n % 2 == 0:
            result = mul(tmp, tmp)
        else:
            a = [1, 1, 1, 0]
            result = mul(mul(tmp, tmp), init)
    return result


def mul(a, b):
    c = [(a[0] * b[0] + a[1] * b[2]) % 1000000007, (a[0] * b[1] + a[1] * b[3]) % 1000000007,
         (a[2] * b[0] + a[3] * b[2]) % 1000000007, (a[2] * b[1] + a[3] * b[3]) % 1000000007]
    return c


n = int(sys.stdin.readline().strip())
init = [1, 1, 1, 0]
fibo = sol(init, n - 1)
print(fibo[0])