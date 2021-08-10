people = 'hello hello'
list = []
result = []
for i in range(len(people)):
    list.append(people[i])
for i in range(len(list)):
    if list[i] == ' ':
        continue
    list[i] = list[i].upper()
    res = ''.join(list)
    result.append(res)
    list[i] = list[i].lower()
print(result)