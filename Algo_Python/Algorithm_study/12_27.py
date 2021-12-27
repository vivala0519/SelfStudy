string = 'moOse'
string = list(string)
print(string)
arr = []
for i in range(len(string)):
    if string[i].lower() not in arr:
        arr.append(string[i])
    else:
        pass
print(arr)
if len(string) == len(arr):
    print(True)
else:
    print(False)