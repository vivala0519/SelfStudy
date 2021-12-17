i = 1634
i = str(i)
tot = 0
for n in range(len(i)):
    temp = pow(int(i[n]), len(i))
    print(temp)
    tot += temp
print(tot)
if tot == int(i):
    print(True)
else:
    print(False)