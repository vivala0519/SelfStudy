# s = "qu'est-ce qu'il mange aujourd'hui"
import sys
s = sys.stdin.readline().rstrip()

front = ['c', 'j', 'n', 'm', 't', 's', 'l', 'd', 'qu']
back = ['a', 'e', 'i', 'o', 'u', 'h']
s = s.split(' ')
for i in range(len(s)):
    s[i] = s[i].split('-')
arr = []
for i in s:
    arr += i
result = []
for i in range(len(arr)):
    if "'" in arr[i]:
        x, y = arr[i].split("'")[0], arr[i].split("'")[1]
        if x in front and y[0] in back:
            result.append(x)
            result.append(y)
        else:
            result.append(arr[i])
    else:
        result.append(arr[i])
print(len(result))