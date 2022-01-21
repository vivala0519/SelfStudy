from itertools import product
dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

digits = '23'

arr = list(digits)
# print(arr)
temp = []
for i in arr:
    temp.append(dic[i])
# print(temp)
arr = list(product(*temp))
# print(arr)
result = list(map(lambda x:''.join(x),arr))
# print(result)

stack = ['']
for i in digits:
    print('i:', i)
    temp = []
    for j in dic[i]:
        print('j:', j)
        for k in stack:
            print('k:', k)
            temp.append(k + j)
            print('temp', temp)
    stack = temp
    print(stack)