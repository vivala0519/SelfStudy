n = 39
m = 12
data = []
for i in range(1, n+1):
    if (n % i == 0) & (m % i == 0):
        data.append(i)
print(data)
if max(data) == 1:
    print(True)
else:
    print(False)