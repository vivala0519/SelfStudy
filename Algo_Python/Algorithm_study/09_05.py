bonus = 1500
price = 2
total = 0
double = 0
for i in range(1, 100):
    if total <= bonus:
        print(i)
        double = pow(i, 2)
        total += double * price
        result = i
print(double)
print(total)
result = result - 1
print(result)