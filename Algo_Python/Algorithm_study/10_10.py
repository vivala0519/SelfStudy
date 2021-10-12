s = 'abraxxxas'
for i in range(0, s.__len__()):
    if s[i] == 'x':
        if s[i+1:i+3] == 'xx':
            print('true')
        else:
            print('flase')
        break