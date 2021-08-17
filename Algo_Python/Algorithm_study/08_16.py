txt = 'adira wants to go to the park'
arr = []
for i in range(0, txt.__len__()):
    arr += txt[i]
print(arr)
for i in range(0, arr.__len__()):
    if arr[i] == 'a' or arr[i] == 'e' or arr[i] == 'i' or arr[i] == 'o' or arr[i] == 'u':
        arr[i] = 'o'
vow = ''.join(arr)
print(vow)