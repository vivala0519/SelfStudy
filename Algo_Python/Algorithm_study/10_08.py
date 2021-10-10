# Error Digit Range

num = 909
print(num)
to_string = str(num)
to_max_arr = []
to_min_arr = []
for i in range(0, len(to_string)):
    to_max_arr.append(to_string[i])
    to_min_arr.append(to_string[i])

if to_max_arr[0] != '9':
    for i in range(0, len(to_max_arr)):
        if to_max_arr[i] == to_string[0]:
            to_max_arr[i] = '9'
else:
    for i in range(0, len(to_max_arr)):
        if to_max_arr[i] != to_max_arr[0]:
            temp = to_max_arr[i]
            for j in range(0, len(to_max_arr)):
                if temp == to_max_arr[j]:
                    to_max_arr[j] = '9'
            break
print(to_max_arr)
maximum = ''.join(to_max_arr)
print(maximum)

if to_min_arr[0] == '1':
    for i in range(0, len(to_min_arr)):
        if to_min_arr[i] != to_min_arr[0] and to_min_arr[i] != '0':
            temp = to_min_arr[i]
            for j in range(0, len(to_min_arr)):
                if temp == to_min_arr[j]:
                    to_min_arr[j] = '0'
            break
else:
    temp = to_string[0]
    print('temp', temp, to_min_arr)
    for j in range(0, len(to_min_arr)):
        if to_min_arr[j] == temp:
            print(to_min_arr[j])
            to_min_arr[j] = '1'
            print(to_min_arr)
print(to_min_arr)
minimum = ''.join(to_min_arr)
print(minimum)
result = int(maximum) - int(minimum)
print(result)