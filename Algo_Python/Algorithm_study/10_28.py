import math
n = 0
if n < 0:
    print('no')
temp = math.sqrt(n)
print(str(temp))
if len(str(temp).split('.')[1]) == 1 and str(temp)[2] == '0':
    print('yes')
else:
    print('no')