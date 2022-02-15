import collections, sys
n = int(sys.stdin.readline().rstrip())
stack = collections.deque()
for i in range(1, n + 1):
    stack.append(i)

while True:
    if len(stack) == 1:
        print(stack[0])
        break
    x, y = stack.popleft(), stack.popleft()
    stack.append(y)