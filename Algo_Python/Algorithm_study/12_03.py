
n = 76
sqr = pow(n, 2)
print(sqr)
print(str(sqr)[-2:])
if str(sqr)[-len(str(n)):] == str(n):
    print('Automorphic')
else:
    print('Not!!')