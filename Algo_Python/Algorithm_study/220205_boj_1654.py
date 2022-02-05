import sys
k, n = list(map(int,sys.stdin.readline().rstrip().split()))

arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort()
start, end = 1, arr[-1]

while start <= end:
    total = 0
    # print('s, e:', start, end)
    mid = (start + end) // 2
    # print('mid:', mid)
    for i in arr:
        if i >= mid:
            total += i // mid
    # print('total:', total)
    if total < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)



