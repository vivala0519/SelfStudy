import sys

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = list(set(arr))

temp = []
for i in arr:
    if is_prime_num(i) == True:
        temp.append(i)

if not temp:
    print(-1)
else:
    result = 1
    for i in temp:
        result *= i
    print(result)