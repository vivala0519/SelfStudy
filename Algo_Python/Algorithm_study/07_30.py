word = 'lettuce'
import string
print(string.ascii_lowercase)
letter = ''
for i in range(0, word.__len__()-1):
    if word[i] == word[i + 1]:
        letter = word[i]
        print(letter)
    else:
        pass

for i in string.ascii_lowercase:
    if i == letter:
        num = string.ascii_lowercase.find(i) + 1
        print(string.ascii_lowercase.find(i) + 1)
result = num * 3
print(result)