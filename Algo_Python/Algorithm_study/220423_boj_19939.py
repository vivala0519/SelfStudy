import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
limit = K * (K + 1) // 2

if N < limit:
    print(-1)
elif (N - limit) % K == 0:
    print(K - 1)
else:
    print(K)
