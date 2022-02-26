import sys

n = int(sys.stdin.readline().rstrip())
result =[]
for i in range(n):
    x = sum(list(map(int, list(str(i)))))
    if i + x == n:
        result.append(i)
        break
if result:
    print(result[0])
else:
    print(0)