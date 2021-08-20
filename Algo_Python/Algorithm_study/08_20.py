s = " qrHqJy cwbGJRn adfDobENd   K dPvfbB "
arr = []
for i in range(0, len(s)):
    arr.append(s[i])
print(arr)
result = ''
length = len(arr)
print(arr[length-1])
for i in range(0, len(arr)):
    # if i == len(arr) - 1:
    #     if arr[len(arr) - 1] == ' ':
    #         print('hi')
    #
    #         pass
    #     else:
    #         result += arr[i].upper()
    #         print('end')
    # else:
    if arr[i] == ' ':
        pass
    else:
        result += arr[i].upper() + '  '
result = result.rstrip()
print(result)