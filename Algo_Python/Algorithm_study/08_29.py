start = '10.11.12.13'
end = '10.11.13.0'

start = start.split('.')
start.reverse()
start = list(map(int, start))
end = end.split('.')
end.reverse()
end = list(map(int, end))
print(start, end)

arr = []
start_num = 0
end_num = 0
for i in range(0, start.__len__()):
    if i == 0:
        start_num += start[0]
        end_num += end[0]
        print(start_num, end_num)
    if i == 1:
        if start[i] != 0:
            start_num += 256 * start[i]
        if end[i] != 0:
            end_num += 256 * end[i]
        print(start_num, end_num)
    if i == 2:
        if start[i] != 0:
            start_num += 256 * 256 * start[i]
        if end[i] != 0:
            end_num += 256 * 256 * end[i]
        print(start_num, end_num)
    if i == 3:
        if start[i] != end[i]:
            if start[i] != 0:
                start_num += 256 * 256 * 256 * start[i]
            if end[i] != 0:
                end_num += 256 * 256 * 256 * end[i]
arr.append(start_num)
arr.append(end_num)
print(arr)
result = arr[1] - arr[0]
print(result)