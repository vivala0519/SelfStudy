import sys
n = int(sys.stdin.readline().rstrip())
x, y = [], []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

x_m = x[len(x) // 2]
y_m = y[len(y) // 2]

total = 0
for i in range(len(x)):
    total += abs(x_m - x[i])
    total += abs(y_m - y[i])
print(total)