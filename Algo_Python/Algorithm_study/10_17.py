number = 556847
arr = []
if len(str(number)) == 1:
    result = 'Jumping!!'
else:
    for i in range(0, len(str(number))):
        arr.append(str(number)[i])
    try:
        for i in range(0, len(arr)):
            if abs(int(arr[i]) - int(arr[i+1])) == 1:
                pass
            else:
                result = 'Not!!'
    except:
        pass
print(arr)