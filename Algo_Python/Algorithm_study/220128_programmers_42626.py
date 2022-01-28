import heapq
scoville = [1, 2, 3, 9, 10, 12]
K = 7
heapq.heapify(scoville)
print(scoville)

cnt = 0
while scoville[0] < K:
    heapq.heappush(scoville, heapq.heappop(scoville) + 2 * heapq.heappop(scoville))
    cnt += 1
print(scoville, cnt)