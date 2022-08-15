import sys

def cal(num, t):
    if t == 1:
        return num % alter
    elif t % 2:
        return num * cal(num, t - 1) % alter
    else:
        temp = cal(num, t // 2)
        return temp * temp % alter

M = int(sys.stdin.readline())
alter = 1000000007
result = 0

for _ in range(M):
    N, S = map(int, sys.stdin.readline().split())
    result += S * cal(N, alter - 2) % alter
print(result % alter)