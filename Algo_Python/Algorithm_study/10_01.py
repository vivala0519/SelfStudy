arr = [10110, 10102, 10097, 10113, 10123, 10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]
k = 2
p_arr = []
for i in range(0, arr.__len__()):
    cnt = 0
    d = 2
    x = arr[i]
    print(x)
    while d <= x:
        if x % d == 0:
            print('num', d)
            x = x / d
            cnt += 1
        else:
            d = d + 1
    p_arr.append(cnt)
print(p_arr)
result_arr = []
cnt = 0
max_cnt = 0
try:
    for i in range(0, p_arr.__len__()):
        if k == p_arr[i]:
            print(i)
            if p_arr[i] == p_arr[i+1]:
                print(i, i+1)
                cnt += 1
                print('cnt', cnt)
                result_arr.append(cnt)
            else:
                cnt = 0
except:
    pass
print('result_arr', result_arr)
if not result_arr:
    result = 0
    print(result)
else:
    result = max(result_arr) + 1
    print(result)