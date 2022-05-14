import sys

N = int(sys.stdin.readline())
vote = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in range(len(arr)):
    if arr[i] in dic:
        dic[arr[i]][0] += 1
    else:
        if len(dic) < N:
            dic[arr[i]] = [1, i]
        else:
            temp = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))
            del(dic[temp[0][0]])
            dic[arr[i]] = [1, i]

dic = sorted(dic.keys())
print(' '.join(str(i) for i in dic))
