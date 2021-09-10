n_floors = 4
length = (n_floors - 1) * 2 + 1
result = []
string = ''
if n_floors == 1:
    result = ['*']
for j in range(1, length+1, 2):
    print(int(((n_floors + 2) - j) / 2))
    string = (int((length - j) / 2) * ' ') + ('*' * j) + (int((length - j) / 2) * ' ')
    result.append(string)
print(result)