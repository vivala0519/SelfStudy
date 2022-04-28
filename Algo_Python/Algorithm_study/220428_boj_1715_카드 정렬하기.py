import heapq
import sys

N = int(sys.stdin.readline().rstrip())

arr = []
for _ in range(N):
    heapq.heappush(arr, int(sys.stdin.readline().rstrip()))

result = 0

while len(arr) != 1:
    first = heapq.heappop(arr)
    sec = heapq.heappop(arr)
    temp = first + sec
    result += temp
    heapq.heappush(arr, temp)

print(result)