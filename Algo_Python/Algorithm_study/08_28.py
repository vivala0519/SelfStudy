lines = ['+---------------------------+', '| THIS IS A MULTI LINE TEST |', '+---------------------------+']
rotors = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53], [8, 46, 7, 12, 30, 1, 4, 16, 34, 52, 32, 13, 11, 48, 3, 14, 4, 24, 16, 13, 3, 47, 22, 26, 50, 13, 52, 47, 8], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 53]]
string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'
line = []
for i in lines:
    line.append(list(i))
print(line)
trans = []
for n in range(0, line.__len__()):
    trans_col = []
    for i in range(0, line[n].__len__()):
        trans_col.append(string.index(line[n][i]))
    trans.append(trans_col)
result = []
print(trans)
for n in range(0, line.__len__()):
    result_col = []
    for during in range(0, rotors[n].__len__()):
        for i in range(0, trans[0].__len__()):
            trans[n][i] = trans[n][i] + rotors[n][during]
        result_col.append(trans[n][during])
    result.append(result_col)
print(result)
for i in range(0, result.__len__()):
    for j in range(0, result[i].__len__()):
        if result[i][j] > len(string):
            result[i][j] = result[i][j] % len(string)
        if result[i][j] == 54:
            result[i][j] = 0
print(result)
real_result = []
for i in range(0, result.__len__()):
    real_result_str = ''
    for j in range(0, result[i].__len__()):
        real_result_str += string[result[i][j]]
    real_result_str
    real_result.append(real_result_str)
print(real_result)