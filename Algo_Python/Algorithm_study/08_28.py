string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
lines = ['CODE']
rotors = [[20, 20, 28, 0]]
line = lines[0]
rotors = rotors[0]
line = list(line)
print(line)
trans = []
for i in range(0, line.__len__()):
    trans.append(string.index(line[i]))
result = []
for during in range(0, rotors.__len__()):
    for i in range(0, trans.__len__()):
        trans[i] = trans[i] + rotors[during]
    print(trans)
    result.append(trans[during])
print(result)
for i in range(0, result.__len__()):
    if result[i] > len(string):
        result[i] = result[i] % len(string)
    if result[i] == 54:
        result[i] = 0
print(result)
real_result_str = ''
for i in range(0, result.__len__()):
    real_result_str += string[result[i]]
real_result = []
real_result.append(real_result_str)
print(real_result)