num = 12
space = str(num).__len__()
list = []
for i in range(space-1, -1, -1):
    print(i)
    share = int(num / (10 ** i))
    if i == 0:
        if num == 0:
            pass
        else:
            res = num
            list.append(res)
            print('res = ', num)
    else:
        if share == 0:
            pass
        else:
            num = num - share * 10 ** i
            print('i : ', i, '몫: ', share, 'num : ', num)
            res = share * (10 ** i)
            list.append(res)
            print('res = ', res)
print(list)
result = ''
for i in range(list.__len__()):
    if i == list.__len__()-1:
        result += str(list[i])
    else:
        result += str(list[i]) + ' + '
print(result)

