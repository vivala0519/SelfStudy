numbers = [357, 579]

if str(numbers[0]).isdigit() == True and str(numbers[1]).isdigit() == True:
    print(abs(int(str(numbers[0])[0] + str(numbers[1])[1:]) - int(str(numbers[1])[0] + str(numbers[0])[1:])))
else:
    print('invalid array')