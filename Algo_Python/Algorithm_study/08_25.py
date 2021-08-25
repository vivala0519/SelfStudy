string = 'MoviesAndBooks'
arr = []
trans = []
string = str(string)
for i in range(0, string.__len__()):
    arr.append(string[i])
arr[0] = arr[0].lower()
trans.append(arr[0])
for i in range(1, string.__len__()):
    if arr[i].isupper():
        arr[i] = arr[i].lower()
        trans.append('_')
        trans.append(arr[i])
    else:
        trans.append(arr[i])
print(trans)
result = ''
for i in range(0, trans.__len__()):
    result += trans[i]
print(result)