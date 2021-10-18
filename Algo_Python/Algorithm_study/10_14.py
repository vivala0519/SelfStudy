arr = [17, 17, 3, 17, 17, 17, 17]
temp = []
for i in range(0, len(arr)):
    x = i
    try:
        if arr[i] != arr[i+1]:
            print(arr[i+1])
            temp.append(arr[i+1])
            temp.append(arr[i])
    except:
        pass
print(temp)
for i in temp:
    if arr.count(i) == 1:
        result = i
print(result)