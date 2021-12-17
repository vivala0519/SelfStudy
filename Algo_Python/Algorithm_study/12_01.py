num1 = 122
num2 = 81

re_num1 = ''
for i in str(num1):
    re_num1 = i + re_num1

re_num2 = ''
for i in str(num2):
    re_num2 = i + re_num2

print(re_num1, re_num2)
length = max(len(re_num1), len(re_num2))
if len(re_num1) < len(re_num2):
    re_num1 = re_num1 + ('0' * (len(re_num2) - len(re_num1)))
if len(re_num2) < len(re_num1):
    re_num2 = re_num2 + ('0' * (len(re_num1) - len(re_num2)))
print(re_num1, re_num2)

result = ''
for i in range(length):
    result = str(int(re_num1[i]) + int(re_num2[i])) + result
print(result)