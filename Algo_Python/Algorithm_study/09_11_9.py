name = [[]]
sentence = ''
if len(name[0]) == 0:
    sentence = 'no one likes this'
elif len(name) == 1:
    sentence = name[0] + ' likes this'
elif len(name) == 2:
    sentence = name[0] + ' and ' + name[1] + ' like this'
elif len(name) == 3:
    sentence = name[0] + ', ' + name[1] + ' and ' + name[2] + ' like this'
else:
    sentence = name[0] + ', ' + name[1] + ' and ' + str(len(name) - 2) + ' others like this'
print(sentence)