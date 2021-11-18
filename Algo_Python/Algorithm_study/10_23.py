numArr = [70, 80, 60]
hap = 0
for i in numArr:
    hap += i
avg = round(hap/3, 2)
print(avg)
if avg >= 90:
    grade = 'A'
elif avg >= 80 and avg < 90:
    grade = 'B'
elif avg >= 70 and avg < 80:
    grade = 'C'
elif avg >= 60 and avg < 70:
    grade = 'D'
else:
    grade = 'F'
print(grade)
# answer = []
# answer.append(str(avg))
# answer.append(grade)
answer = str(avg) + ', ' + grade
print(answer)