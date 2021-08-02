string_ = "Wht r y,  cmmunst?"
arr = []
for i in range(0, string_.__len__()):
    arr.append(string_[i])

for i in range(0, string_.__len__()):
    try:
        if arr[i].lower() == 'a' or arr[i].lower() == 'e' or arr[i].lower() == 'i' \
                or arr[i].lower() == 'o' or arr[i].lower() == 'u':
            arr.remove(arr[i])
    except IndexError:
        continue
print(arr)
result = ''.join(arr)
print(result)