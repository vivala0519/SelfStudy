string = "most Trees Are Blue"
arr = []
for i in range(0, len(string)):
    arr.append(string[i])

for i in range(0, len(arr)):
    if i == 0:
        arr[i] = arr[i].upper()
    if arr[i] == ' ':
        arr[i+1] = arr[i+1].upper()

result = ''.join(arr)
print(result)