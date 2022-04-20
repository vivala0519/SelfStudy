import sys

n = sys.stdin.readline().rstrip()
arr = list(map(int, sys.stdin.readline().rstrip().split()))

arr.sort()
tot = sum(arr)
result = 0
for i in arr:
    result += i * (tot - i)
    tot -= i
print(result)