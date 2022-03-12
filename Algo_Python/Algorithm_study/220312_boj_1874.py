import sys

# n = 8
# arr = [4, 3, 6, 8, 7, 5, 2, 1]
# stack = [8, 7, 6, 5, 4, 3, 2, 1]

n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
count = 1
stack = []
result = []
temp = True
for i in arr:
    while count <= i:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == i:
        stack.pop()
        result.append('-')
    else:
        temp = False
        break
if temp == False:
    print('NO')
else:
    for i in result:
        print(i)