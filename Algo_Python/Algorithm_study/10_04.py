s = 'AAABBC'
arr = list(s) # 문자열 리스트화

# 공백인 요소 제거
for i in range(0, len(arr)):
    if arr[i] == ' ':
        arr[i] = ''
arr = list(filter(None, arr))

# 대문자 문자만 필터링
filtering = []
for i in arr:
    if i.isupper() == True:
        filtering.append(i)

# 대문자 문자 리스트
char_list = set(filtering)
char_list = sorted(char_list)

# 각 요소 갯수
count_list = []
for i in char_list:
    count = 0
    for j in filtering:
        if i == j:
            count += 1
    count_list.append(count)
print('full:', filtering)
print('char_list', char_list)
print('count_list', count_list)

# 히스토그램 만들기
result_arr = []
for i in range(1, max(count_list) + 1):
    temp = []
    for j in range(0, count_list.__len__()):
        if j != count_list.__len__() - 1:
            if i <= count_list[j]:
                temp.append('* ')
            else:
                temp.append('  ')
        else:
            if i <= count_list[j]:
                temp.append('*')
            else:
                temp.append(' ')
    result_arr.append(temp)
print(result_arr)

to_string = []
for i in range(0, result_arr.__len__()):
    temp = ''
    for j in range(0, result_arr[i].__len__()):
        temp += result_arr[i][j]
    to_string.append(temp)
print(to_string)
to_string.reverse()
print(to_string)
char_str = ''
for i in range(0, char_list.__len__()):
    if i != char_list.__len__() - 1:
        char_str += char_list[i] + ' '
    else:
        char_str += char_list[i]
to_string.append(char_str)
print(to_string)

result = ''
for i in range(0, to_string.__len__()):
    if i != to_string.__len__() - 1:
        result += to_string[i] + '\n'
    else:
        result += to_string[i]
print(result)
