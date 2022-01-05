#string = "cherries , avocados apples\navocados lemons ,\ncherries watermelons oranges apples\n' oranges ! bananas oranges\npears pears bananas"
string = "apples, pears # and bananas\ngrapes\nbananas !#apples"
# markers = [',', '!', '.', "'", '-', '^', '#', '@']
markers = ['#', '!']

markers.sort()
print(markers)

if not markers:
    print(string)
result_arr = []
str_arr = string.split('\n')
for i in range(len(str_arr)):
    temp = 0
    temp_arr = []
    for j in markers:
        if j in str_arr[i]:
            if str_arr[i].index(j) == 0:
                temp_arr.append('')
                break
            else:
                # result_arr.append(str_arr[i][:str_arr[i].index(j)-1].rstrip())
                temp_arr.append(str_arr[i][:str_arr[i].index(j)-1].rstrip())
        else:
            temp += 1
        if temp == len(markers):
            result_arr.append(str_arr[i])
    if len(temp_arr) > 1:
        min_str = temp_arr[0]
        for k in temp_arr:
            if min_str > k:
                min_str = k
        result_arr.append(min_str)
    elif len(temp_arr) == 1:
        result_arr.append(temp_arr[0])
print(result_arr)
result = ''
for i in range(len(result_arr)):
    if i == len(result_arr):
        pass
    else:
        result += result_arr[i] + '\n'
print(result[:-1])
print('\n\n---------------------------------------------\n\n')
# print('cherries\navocados lemons\ncherries watermelons oranges apples\n\npears pears bananas')
print('apples, pears\ngrapes\nbananas')