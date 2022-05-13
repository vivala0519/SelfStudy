import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
dic = {}
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
    dic[arr[i][1]] = arr[i][0]

location = []
for i in arr:
    location.append(i[1])
location.sort()
left = location[0]
right = location[0] + (K * 2)

stack = []
while left <= location[-1] - (K * 2):
    temp = 0
    for i in range(left, right + 1):
        if i in dic:
            temp += dic[i]
    stack.append(temp)
    left += 1
    right += 1
print(max(stack))