import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

def dfs(x):
    global result

    if len(arr) == 2:
        result = max(result, x)
        return

    for i in range(1, len(arr) - 1):
        target = arr[i - 1] * arr[i + 1]
        y = arr.pop(i)
        dfs(x + target)
        arr.insert(i, y)

dfs(0)
print(result)