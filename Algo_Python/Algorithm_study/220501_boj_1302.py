from collections import defaultdict
from operator import truediv
import sys

dic = defaultdict(int)

N = int(sys.stdin.readline())

for _ in range(N):
    dic[sys.stdin.readline().rstrip()] += 1

# print(dic)

result = []
for i in dic:
    result.append([i, dic[i]])
# print(result)
result.sort(key=lambda x:x[0])
result.sort(key=lambda x:x[1], reverse=True)
# print(result)
print(result[0][0])