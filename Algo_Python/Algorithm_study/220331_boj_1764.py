from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
hear, see = [], []
for _ in range(N):
    hear.append(sys.stdin.readline().rstrip())
for _ in range(M):
    see.append(sys.stdin.readline().rstrip())

# hear = ['ohhenrie', 'charlie', 'baesangwook']
# see = ['obama', 'baesangwook', 'ohhenrie', 'clinton']

dic = defaultdict(int)
for i in hear:
    dic[i] += 1

for j in see:
    dic[j] += 1

# print(dic)

result = []
for i in dic:
    if dic[i] == 2:
        result.append(i)
result.sort()
for i in result:
    print(i)