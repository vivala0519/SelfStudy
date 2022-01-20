import math
# progresses = [93, 30, 55]
progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 30, 5]
speeds = [1, 1, 1, 1, 1, 1]

days = []
for i in range(len(progresses)):
    days.append(math.ceil((100 - progresses[i]) / speeds[i]))
print(days)

result = []

while days:
    temp = days[0]
    for i in range(len(days)):
        days[i] -= temp

    temp_num = 0
    while days:
        if days[0] <= 0:
            days.pop(0)
            temp_num += 1
        else:
            break
    result.append(temp_num)
print(days, result)