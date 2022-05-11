import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

print(arr)
temp = sorted(list(set(arr)))
# print(arr2)
# dic = {temp[i] : i for i in range(len(temp))}
dic = {}
for i in range(len(temp)):
    dic[temp[i]] = i
print(dic)
for i in arr:
    print(dic[i], end = ' ')