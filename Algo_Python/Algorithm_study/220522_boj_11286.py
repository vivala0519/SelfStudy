import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(temp), temp))
