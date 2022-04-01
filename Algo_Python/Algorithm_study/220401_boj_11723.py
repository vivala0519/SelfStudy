import sys
from collections import defaultdict

S = defaultdict(int)

M = int(sys.stdin.readline().rstrip())

for _ in range(M):
    x = sys.stdin.readline().rstrip()
    if x != 'all' and x != 'empty':
        temp = x.split()[1]
    if x[:2] == 'ad':
        S[int(temp)] = 1
    elif x[:2] == 're':
        S[int(temp)] = 0
    elif x[:2] == 'ch':
        if S[int(temp)] == 1:
            print(1)
        else:
            print(0)
    elif x[:2] == 'to':
        if S[int(temp)] == 1:
            S[int(temp)] = 0
        else:
            S[int(temp)] = 1
    elif x[:2] == 'al':
        # for i in range(1, 21):
        #     S[i] = 1
        S = defaultdict(lambda: 1)
    else:
        S = defaultdict(lambda: 0)
