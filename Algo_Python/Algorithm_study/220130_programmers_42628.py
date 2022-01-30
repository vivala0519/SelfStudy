import heapq, collections
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

h = []
for item in operations:
    temp = item.split(' ')
    if temp[0] == 'I':
        heapq.heappush(h, int(temp[1]))
        print(h)
    elif temp[0] == 'D':
        if temp[1] == '1':
            h.pop()
            print(h)
        else:
            heapq.heappop(h)
            print(h)
print(h)
h = collections.deque(h)
if not h:
    print([0,0])
else:
    print([h.pop(), h.popleft()])