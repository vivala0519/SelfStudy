n = 25
while n % 3 != 0:
    try:
        n = int(str(n)[:-1])
        print(n)
    except:
        print('null')
        break
print(n)
