import sys
N = int(sys.stdin.readline().rstrip())
sang = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# result = []
# for i in arr:
#     result.append(sang.count(i))
#
# print(' '.join(str(n) for n in(result)))
#

# sang = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
# arr = [10, 9, -5, 2, 3, 4, 5, -10]

dic = {}

for i in sang:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

result = []
for i in arr:
    if i in dic:
        result.append(dic[i])
    else:
        result.append(0)
print(dic)
print(result)
print(' '.join(str(n) for n in(result)))