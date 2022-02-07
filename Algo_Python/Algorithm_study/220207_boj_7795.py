import sys

from attr import s
t = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    b = list(map(int, sys.stdin.readline().rstrip().split()))
    a.sort()
    b.sort()
    temp = []
    # start = 0
    # end = len(b) - 1
    cnt = 0
    for i in a:
        for j in b:
            if i > j:
                cnt += 1
        # start = 0
        # end = len(b) - 1
        # while start <= end:
        #     bin = (start + end) // 2
        #     if b[bin] >= i:
        #         end = bin - 1
        #     else:
        #         start = bin + 1
        #         cnt += 1
        
    arr.append(cnt)
for i in range(len(arr)):
    print(arr[i])