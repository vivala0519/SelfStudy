n = 34625647867585
d = 10

arr = []
if d < 0:
    print(arr)
result = str(n)[-d:]
for i in range(len(result)):
    arr.append(int(result[i]))
print(arr)