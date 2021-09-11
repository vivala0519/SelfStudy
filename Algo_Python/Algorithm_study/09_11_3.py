jobs = [[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]
second = 1
second += jobs[0][1]
print(second)
wait = []
for i in range(1, jobs.__len__()):
    if jobs[i][0] < second:
        wait.append(jobs[i])
print(wait)
group = []
for i in range(0, wait.__len__()):
    for j in range(i+1, wait.__len__()):
        if wait[i][2] == wait[j][2]:
            print(wait[i][2], wait[j][2])
            tot = wait[i][3] + wait[j][3]
            group.append(wait[i])
            group.append(wait[j])
print(group, tot)
rest =[]
for i in range(0, wait.__len__()):
    if wait[i] in group:
        pass
    else:
        rest.append(wait[i])
print(rest)