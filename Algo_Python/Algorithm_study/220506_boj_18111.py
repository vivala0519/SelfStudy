import sys, math

N, M, B = map(int, input().split())
arr = []

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    arr += i
    B += sum(i)

min_height = min(arr)
max_height = math.floor(B / (N * M))
result_time = 1e9
result_height = 0


for height in range(min_height, max_height + 1):
    time = 0
    for i in arr:
        if i > height:
            time += (i - height) * 2
        elif i < height:
            time += height - i
        if time > result_time:
            break
    if time < result_time:
        result_time = time
        result_height = height
    elif time == result_time and height > result_height:
        result_height = height

print(result_time, result_height)