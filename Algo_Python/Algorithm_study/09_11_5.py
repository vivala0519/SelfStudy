id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
report = set(report)
report = list(report)
for i in range(0, report.__len__()):
    report[i] = report[i].split(' ')
print('report : ', report)
reported = []
for i in range(0, report.__len__()):
    reported.append(report[i][1])
print('reported : ', reported)
reported_name = set(reported)
reported_name = list(reported_name)
print('reported_name : ', reported_name)
reported_count = []
for i in reported_name:
    temp = []
    temp.append(i)
    temp.append(reported.count(i))
    reported_count.append(temp)
print('reported_count : ', reported_count)
blocked = []
for i in reported_count:
    if i[1] >= 2:
        blocked.append(i[0])
print('blocked : ', blocked)
temp = []
for i in range(0, report.__len__()):
    if report[i][1] in blocked:
        temp.append(report[i][0])
print(temp)
result = []
for i in id_list:
    result.append(temp.count(i))
print(result)