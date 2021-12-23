friday = [5, 1, 4]
saturday = [5, 4]
total = 29

plus = 0
for i in friday:
    plus += i
for i in saturday:
    plus += i
print(total - plus)