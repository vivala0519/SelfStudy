import itertools
research = ["xy", "xy"]
n = 2
k = 2
arr = []
char_list = []
for i in research:
    arr.append(list(i))
    char_list.append(list(i))
for i in range(0, char_list.__len__()):
    char_list[i] = set(arr[i])
    char_list[i] = list(arr[i])
char_list = list(itertools.chain.from_iterable(char_list))
char_list = set(char_list)
char_list = sorted(list(char_list))
print('arr : ', arr)
print('char_list : ', char_list)

total_arr = []
for i in arr:
    char_num = []
    for j in char_list:
        temp = []
        temp.append(j)
        temp.append(i.count(j))
        char_num.append(temp)
    total_arr.append(char_num)
print(total_arr)
result = []
for i in range(0, n):
    for j in range(0, char_list.__len__()):
            if total_arr[i][j][1] > k:
                try:
                    if total_arr[i][j][1] + total_arr[i+1][j][1] >= 2 * n * k:
                        result.append(total_arr[i][j][0])
                except:
                    pass
print('result = ', result)
if not result:
    print('None')
else:
    result_count = []
    for i in char_list:
        result_count.append(result.count(i))
    print(result_count)
    index = result_count.index(max(result_count))
    answer = char_list[index]
    print(answer)