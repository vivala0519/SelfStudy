sentence = 'This sentence is a sentence'

sentence = sentence.split(' ')
for i in range(len(sentence)):
    if len(sentence[i]) >= 5:
        sentence[i] = sentence[i][::-1]
print(' '.join(sentence))