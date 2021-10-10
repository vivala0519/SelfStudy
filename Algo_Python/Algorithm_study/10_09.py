# Image Matching

locations = [2, 0, 0, 0]

size = len(locations)

arr = []
for i in range(1, size+1):
    if max(i-locations[i-1], 1) == min(i+locations[i-1], size):
        arr.append(min(i+locations[i-1], size))
    else:
        arr.append(range(max(i-locations[i-1], 1), min(i+locations[i-1], size) + 1))
    print(max(i-locations[i-1], 1), 'to', min(i+locations[i-1], size))
print(arr)
new = []
for i in arr:
    if type(i) == int:
        temp = i
        for j in arr:
            if type(j) == range:
                if temp not in j:
                    new.append(temp)
    else:
        new.append((i[0], i[-1]))
print('new:', new)
temp = []
temp_int = []
for i in new:
    if type(i) == tuple:
        print(i)
        temp.append(i)
    else:
        temp_int.append(i)
sorted(temp)
starts, ends = [], []
for k, (x, y) in enumerate(temp):
    if k > 0:
        if x <= ends[-1]:
            ends[-1] = y
            continue
    starts.append(x)
    ends.append(y)
result = list(zip(starts, ends))
for i in temp_int:
    result.append(i)
print(result)

