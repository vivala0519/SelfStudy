import sys, heapq

T = int(sys.stdin.readline())
for _ in range(T):
    k, maxh, minh = int(sys.stdin.readline()), [], []
    check = [0] * k
    for i in range(k):
        x, y = sys.stdin.readline().split()

        if x == 'I':
            heapq.heappush(maxh, ((-1) * int(y), i))
            heapq.heappush(minh, (int(y), i))
            check[i] = 1
        else:
            if y == '-1':
                while minh and not check[minh[0][1]]:
                    heapq.heappop(minh)
                if minh:
                    check[minh[0][1]] = 0
                    heapq.heappop(minh)
            else:
                while maxh and not check[maxh[0][1]]:
                    heapq.heappop(maxh)
                if maxh:
                    check[maxh[0][1]] = 0
                    heapq.heappop(maxh)

    while minh and not check[minh[0][1]]:
        heapq.heappop(minh)
    while maxh and not check[maxh[0][1]]:
        heapq.heappop(maxh)

    if minh and maxh:
        print(-maxh[0][0], minh[0][0])
    else:
        print('EMPTY')