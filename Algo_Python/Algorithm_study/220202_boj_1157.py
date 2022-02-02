import collections
import sys, collections
str = sys.stdin.readline().rstrip().upper()
dic = collections.defaultdict(int)
for i in range(len(str)):
    dic[str[i]] += 1
# print(dic)
str = list(set(str))
print(str)
result = []
for i in range(len(str)):
    result.append(dic[str[i]])
print(result)
if result.count(max(result)) > 1:
    print('?')
else:
    print(list(dic.keys())[list(dic.values()).index(max(result))])