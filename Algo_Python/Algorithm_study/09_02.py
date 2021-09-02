password = 'hello world_'
arr = []
if password != "":
    for i in range(0, password.__len__()):
        arr.append(password[i])
    print(arr)
    for i in range(0, arr.__len__()):
        if arr[i].isalnum() == False:
            print(arr[i])
else:
    print('false')