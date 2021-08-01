str = '4244'
res = ''
print(str.__len__())
if str.__len__() == 4 or str.__len__() == 6:
    res = 'true'
else:
    res = 'false'
print(res)
for i in range(0, str.__len__()):
    if str[i].isalpha() == True:
        res = 'false'
print(res)