import sys, math

n = int(sys.stdin.readline())

for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    temp = 0
    for j in range(1, len(arr)):
        for k in range(j + 1, len(arr)):
            temp += math.gcd(arr[j], arr[k])

    print(temp)