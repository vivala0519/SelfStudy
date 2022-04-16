import sys

L = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

result = 0

for i in range(L):
    result += (ord(s[i])-96) * (31 ** i)

print(result % 1234567891)