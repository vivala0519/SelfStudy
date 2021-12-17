n = 2017

n = bin(n)
n = str(n)[2:]
print(n)
temp = ''
for i in range(len(n)):
    temp = n[i] + temp
print(int(temp, 2))