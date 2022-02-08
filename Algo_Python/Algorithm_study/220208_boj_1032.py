import sys
N = int(sys.stdin.readline().rstrip())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip())

test = list(arr[0])

for i in range(1, len(arr)):
    for j in range(len(test)):
        if test[j] != arr[i][j]:
            test[j] = '?'
print(''.join(test))