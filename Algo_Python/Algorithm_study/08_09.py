import numpy as np

scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

temp = []
row = []
for j in range(0, scores.__len__()):
    for i in scores:
        temp.append(i[j])
    row.append(temp)
    temp = []
print(row)

for i in range(0, scores.__len__()):
    if scores[i][i] == max(row[i]):
        count = 0
        for j in range(0, scores.__len__()):
            if scores[i][i] == row[i][j]:
                count += 1
                print('count : ', count)
        if count > 1:
            pass
        else:
            row[i].remove(max(row[i]))
    if scores[i][i] == min(row[i]):
        count = 0
        for j in range(0, scores.__len__()):
            if scores[i][i] == row[i][j]:
                count += 1
        if count > 1:
            pass
        else:
            row[i].remove(min(row[i]))
avg = []
for i in range(0, row.__len__()):
    avg.append(np.mean(row[i]))
print(avg)
grade = []
for i in range(0, row.__len__()):
    if avg[i] >= 90:
        grade.append('A')
    if avg[i] >= 80 and avg[i] < 90:
        grade.append('B')
    if avg[i] >= 70 and avg[i] < 80:
        grade.append('C')
    if avg[i] >= 50 and avg[i] < 70:
        grade.append('D')
    if avg[i] < 50:
        grade.append('F')
print(grade)
answer = ''.join(grade)
print(answer)
