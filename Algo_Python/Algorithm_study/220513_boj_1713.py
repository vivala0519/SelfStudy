from collections import defaultdict, deque

N = 3
K = 9
arr = deque([2, 1, 4, 3, 5, 6, 2, 7, 2])
dic = defaultdict(int)

stack = deque([])
while arr:
    x = arr.popleft()
    if len(stack) < N:
        if x not in stack:
            stack.append(x)
        dic[x] += 1
    else:
        temp = []
        for i in stack:
            temp.append(dic[i])