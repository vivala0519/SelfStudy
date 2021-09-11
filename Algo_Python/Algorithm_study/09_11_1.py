student = [0, 1, 0]
k = 2
arr = []
count = 0
for j in range(0, student.__len__()):
    for i in range(0, student.__len__()+1):
        # print(student[j:i])
        if student[j:i].count(1) == k:
            arr.append(student[j:i])
            count += 1
print(count)
print(arr)