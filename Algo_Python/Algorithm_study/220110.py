a = [4, 1, 7, 5, 6, 4]

a.sort()
print(a)

count = 0
try:
    if a[0] > a[1]:
        count += 1
        for i in range(1, len(a)):
            if i % 2 == 0:
                if a[i] > a[i-1] and a[i] > a[i+1]:
                    print(i, '+')
                    count += 1
    else:
        for i in range(1, len(a)):
            if i % 2 != 0:
                if a[i] > a[i-1] and a[i] > a[i+1]:
                    print(i, '+')
                    count += 1
except:
    pass

if a[len(a)-1] > a[len(a)-2]:
    print(len(a)-1, '+')
    count += 1

if len(a) % 2 != 0:
    if count == int(len(a) / 2) + 1:
        print('Wave')
    else:
        print('no')
else:
    if count == len(a) / 2:
        print('Wave')
    else:
        print('no')

print(count)

#---------------------------------------------------------------------------------Best Solution

a.sort()
for i in range(1, len(a), 2):
    a[i], a[i-1] = a[i-1], a[i]