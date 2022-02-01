import sys, collections

arr = collections.deque()
while str != 'END':
    str = sys.stdin.readline().rstrip()
    arr.append(str)
print(arr)

while arr:
    str = arr.popleft()
    if str == 'END':
        break
    else:
        print(''.join(reversed(str)))