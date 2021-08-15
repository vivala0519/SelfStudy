row = 'RRGBRGBB'
arr = []
for i in range(0,row.__len__()):
    arr += row[i]
print(arr.__len__() - 1)
until = arr.__len__() - 1
while until != 0:
    print('until = ', until)
    for i in range(0, arr.__len__()):
        print(i)
        if i == until:
            del arr[i]
            print(arr)
            break
        else:
            if arr[i] == arr[i+1]:
                str = arr[i]
                arr[i] = str
            elif (arr[i] == 'B' and arr[i+1] == 'G') or (arr[i] == 'G' and arr[i+1] == 'B'):
                arr[i] = 'R'
            elif (arr[i] == 'R' and arr[i+1] == 'G') or (arr[i] == 'G' and arr[i+1] == 'R'):
                arr[i] = 'B'
            elif (arr[i] == 'B' and arr[i+1] == 'R') or (arr[i] == 'R' and arr[i+1] == 'B'):
                arr[i] = 'G'
            print(arr)
    until -= 1
print(arr)
result = arr[0]
print(result)