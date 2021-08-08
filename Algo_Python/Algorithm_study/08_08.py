s = 'camelCasing'
list = []
for i in range(0, s.__len__()):
    if s[i].isupper() == True:
        list.append(' ')
        list.append(s[i])
    else:
        list.append(s[i])
result = ''
for i in range(0, list.__len__()):
    result += list[i]
print(result)