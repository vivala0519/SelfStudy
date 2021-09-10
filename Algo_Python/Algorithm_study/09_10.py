intervals = [[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]

trans = []
for i in range(0, len(intervals)):
    temp = []
    for j in range(intervals[i][0], intervals[i][1] + 1):
        temp.append(j)
    trans.append(temp)
print(trans)

new = []
for i in range(0, trans.__len__()):
    try:
        count = 0
        for k in range(i+1, trans.__len__()):
            for j in range(0, trans[i].__len__()):
                if count == 1:
                    pass
                else:
                    if trans[i][j] in trans[k]:
                        print('붙인다 :', trans[i], '랑', trans[k])
                        new.append(trans[i] + trans[k])
                        count += 1
    except:
        pass
for i in range(0, new.__len__()):
    new[i] = set(new[i])
    new[i] = list(new[i])
print(new)

the = []
total_count = 0
while total_count == 0:
    for i in range(0, new.__len__()):
        try:
            count = 0
            for k in range(i+1, new.__len__()):
                for j in range(0, new[i].__len__()):
                    if count == 1:
                        pass
                    else:
                        if new[i][j] in new[k]:
                            print('붙인다 :', new[i], '랑', new[k])
                            the.append(new[i] + new[k])
                            count += 1
                            total_count += 1
        except:
            pass
    new = the
    for i in range(0, new.__len__()):
        new[i] = set(new[i])
        new[i] = list(new[i])
    total_count = 0
print(new)
print(total_count)