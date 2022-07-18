import sys

A, B = map(int, sys.stdin.readline().split())

result = 1
while True:
    if A == B:
        break
    elif (B % 2 != 0 and B % 10 != 1) or A > B:
        print(-1)
        sys.exit(0)
    else:
        if B % 10 == 1:
            B //= 10
            result += 1
        else:
            B //= 2
            result += 1
print(result)