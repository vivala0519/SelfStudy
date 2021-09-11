intervals = [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]

trans = []
for i in range(0, len(intervals)):
    temp = []
    for j in range(intervals[i][0], intervals[i][1] + 1):
        temp.append(j)
    trans.append(temp)
print(trans)

total_count = 1
result = []
find_rest = []
while total_count != 0:
    new = []
    total_count = 0
    for i in range(0, trans.__len__()):
        try:
            count = 0
            for k in range(i+1, trans.__len__()):
                for j in range(0, trans[i].__len__()):
                    if count == 1:
                        pass
                    else:
                        if trans[i][j] in trans[k]:
                            find = []
                            print('붙인다 :', trans[i], '랑', trans[k])
                            new.append(trans[i] + trans[k])
                            result.append(new)
                            count += 1
                            total_count += 1
                            find.append(i)
                            find.append(k)
                            find_rest.append(find)
        except:
            pass
    trans = new
    for i in range(0, trans.__len__()):
        trans[i] = set(trans[i])
        trans[i] = list(trans[i])
    print(trans)
result = result[result.__len__()-1]
print(result)
print('find_res = ', find_rest[0])
for j in range(0, intervals.__len__()):
    if j in find_rest[0]:
        pass
    else:
        result.append(intervals[j])
print(result)
total_sum = 0
for i in range(0, result.__len__()):
    total_sum += result[i][len(result[i])-1] - result[i][0]
print(total_sum)

result = set()
for start, stop in intervals:
    for x in range(start, stop):
        result.add(x)
        print(result)
print(result)