words = 'wedding bells'
# words = words.split(' ')
# print(words)
words = words.split(' ')[1][0] + words.split(' ')[0][1:] + ' ' + words.split(' ')[0][0] + words.split(' ')[1][1:]
print(words)