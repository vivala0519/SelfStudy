arr = [0, 1, 0, 1]
arr.reverse()
result = 0
for i in range(0, arr.__len__()):
    if arr[i] == 1:
        result += pow(2, i)
print(result)