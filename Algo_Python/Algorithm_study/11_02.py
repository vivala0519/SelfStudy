array = [-10, 42, 5, -7, 3, 18]
n = 4
temp = []
for i in array:
    temp.append(i)
highest = []
lowest = []
for i in range(n):
    max_num = max(array)
    highest.append(max_num)
    array.remove(max_num)
for i in range(n):
    min_num = min(temp)
    lowest.append(min_num)
    temp.remove(min_num)
print(highest, lowest)
low_sum = 1
for i in range(len(lowest)):
    low_sum *= lowest[i]
print(low_sum)
if sum(highest) > low_sum:
    print('sum')
elif sum(highest) < low_sum:
    print('product')
else:
    print('same')