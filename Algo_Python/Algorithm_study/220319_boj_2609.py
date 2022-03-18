import sys

x, y = map(int, sys.stdin.readline().rstrip().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

print(int(gcd(x, y)))
print(int(lcm(x, y)))