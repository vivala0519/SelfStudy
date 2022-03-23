import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    arr = []
    for _ in range(n):
        arr.append(sys.stdin.readline().rstrip())

    temp = []
    for i in arr:
        temp.append(i.lower())
    temp.sort()
    result = temp[0]
    for i in arr:
        if result == i.lower():
            print(i)