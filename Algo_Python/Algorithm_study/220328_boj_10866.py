import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
command = []
for _ in range(n):
    command.append(sys.stdin.readline().rstrip())

q = deque([])
for i in command:
    x = i[:6]
    if x == 'push_f':
        q.appendleft(i.split()[1])
    elif x == 'push_b':
        q.append(i.split()[1])
    elif x == 'pop_fr':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif x == 'pop_ba':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif x == 'size':
        print(len(q))
    elif x == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif x == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)