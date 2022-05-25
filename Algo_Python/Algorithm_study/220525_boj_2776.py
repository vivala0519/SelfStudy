from collections import defaultdict
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    before = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    after = list(map(int, sys.stdin.readline().split()))
    dic = defaultdict(int)
    for i in before:
        dic[i] = 1
    for i in after:
        if i in dic:
            print(1)
        else:
            print(0)