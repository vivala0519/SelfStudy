price = 3
money = 20
count = 4
sum = 0
for i in range(1, count+1):
    num = price * i
    sum += num
    print(sum)
if money >= sum:
    result = 0
else:
    result = sum - money
print(result)