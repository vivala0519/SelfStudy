numbers = [1, 5, 12]

evens = []
odds = []
for i in numbers:
    if i % 2 == 0:
        if i < 0:
            evens.append(-int(format(i, 'b').count('1')))
        else:
            evens.append(format(i, 'b').count('1'))
    else:
        if i < 0:
            odds.append(-int(format(i, 'b').count('1')))
        else:
            odds.append(format(i, 'b').count('1'))
print(sum(evens), sum(odds))
if sum(evens) > sum(odds):
    print('evens win')
elif sum(odds) > sum(evens):
    print('odds win')
else:
    print('tie')