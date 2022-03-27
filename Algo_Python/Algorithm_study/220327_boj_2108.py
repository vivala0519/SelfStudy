import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

# 일단 정렬
arr.sort()

# 산술평균
arith = round(sum(arr) / n)
# 중앙값
mid = arr[len(arr)//2]
# 범위
ran = arr[-1] - arr[0]

# 최빈값
dic = defaultdict(int)
for i in arr:
    dic[i] += 1
temp = [k for k, v in dic.items() if max(dic.values()) == v]
temp.sort()
if len(temp) > 1:
    most = temp[1]
else:
    most = temp[0]


print(arith)
print(mid)
print(most)
print(ran)