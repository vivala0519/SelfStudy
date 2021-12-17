arr = [1,2,3,5,3,2,1]
index = []
for i in range(0, len(arr)):
    if sum(arr[:i+1]) - arr[i] == sum(arr[i:]) - arr[i]:
        index.append(i)
if len(index) == 0:
    print(-1)
else:
    print(index[0])