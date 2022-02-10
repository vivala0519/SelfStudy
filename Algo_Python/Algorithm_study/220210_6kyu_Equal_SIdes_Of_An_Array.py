arr = [1, 2, 3, 4, 3, 2, 1]

temp = []
for i in range(len(arr)):
    temp.append((sum(arr[:i]), sum(arr[i+1:])))
print(temp)
for x,y in enumerate(temp):
    if y[0] == y[1]:
        print(x)