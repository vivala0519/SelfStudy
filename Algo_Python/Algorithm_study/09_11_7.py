from datetime import datetime
import math
from operator import itemgetter
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
for i in range(0, records.__len__()):
    records[i] = records[i].split(' ')
records = sorted(records, key = lambda x: x[1])
print(records)
car_nums = []
for i in range(0, records.__len__()):
    car_nums.append(records[i][1])
car_temp = car_nums
car_nums = set(car_nums)
car_nums = list(car_nums)
car_nums.sort()
print('car_nums : ', car_nums)
print(car_temp)
car_count = []
for j in car_nums:
    temp = []
    temp.append(j)
    temp.append(car_temp.count(j))
    car_count.append(temp)
num_time = []
num_time_rest = []
for i in car_count:
    if i[1] % 2 == 0:
        for j in range(0, records.__len__()):
            if i[0] == records[j][1]:
                temp = []
                temp.append(records[j][1])
                temp.append(records[j][0])
                temp.append(records[j][2])
                print(records[j][1], records[j][0])
                num_time.append(temp)
    else:
        for j in range(0, records.__len__()):
            if i[0] == records[j][1]:
                temp = []
                temp.append(records[j][1])
                temp.append(records[j][0])
                temp.append(records[j][2])
                num_time_rest.append(temp)
        temp = []
        temp.append(i[0])
        temp.append('23:59')
        temp.append('OUT')
        num_time_rest.append(temp)
print(num_time_rest)
print(num_time)
for i in range(0, num_time_rest.__len__()):
    num_time.append(num_time_rest[i])
print(num_time)
num_dif = []
for i in range(0, num_time.__len__()):
    try:
        for j in range(i+1, i+2):
            if num_time[i][0] == num_time[j][0] and num_time[i][2] == 'IN':
                time = datetime.strptime(num_time[j][1], "%H:%M") - datetime.strptime(num_time[i][1], "%H:%M")
                time = str(time).split(':')[0:2]
                time = int(time[0]) * 60 + int(time[1])
                temp = []
                temp.append(num_time[i][0])
                temp.append(time)
                num_dif.append(temp)
    except:
        pass
print(num_dif)
result = []
for i in range(0, num_dif.__len__()):
    for j in range(i+1, num_dif.__len__()):
        if num_dif[i][0] == num_dif[j][0]:
            num_dif[i][1] += num_dif[j][1]
            num_dif[j][1] = num_dif[i][1]
            result.append(num_dif[i])
ans = [x for x in num_dif if num_dif.count(x) == 1]
for i in ans:
    result.append(i)
print('result : ', result)
answer_list = []
for item in result:
    if item[1] > fees[0]:
        temp = []
        pay = fees[1] + math.ceil((item[1] - fees[0]) / fees[2]) * fees[3]
        temp.append(item[0])
        temp.append(pay)
        answer_list.append(temp)
    else:
        pay = fees[1]
        temp = []
        temp.append(item[0])
        temp.append(pay)
        answer_list.append(temp)
print(answer_list)
answer_list.sort(key=itemgetter(0))
answer = []
for i in range(0, answer_list.__len__()):
    answer.append(answer_list[i][1])
print(answer)