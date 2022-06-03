import sys

N, L = map(int, sys.stdin.readline().split())
location = list(map(int, sys.stdin.readline().split()))

location.sort()

start = location[0]
count = 1

for item in location[1:]:
    if item in range(start, start + L):
        continue
    else:
        start = item
        count += 1

print(count)