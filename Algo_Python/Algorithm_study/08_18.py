string = 'ehHF ocr,Nz2F.I8H,SzUY2s9x2aAQu7E5BoIqi'
trans = string.lower()

for i, let in enumerate(trans):
    if trans.count(let) == 1:
        print(string[i])

print(trans)
arr = []
for i in range(0, trans.__len__()-1):
    for j in range(i+1, trans.__len__()):
        if trans[i] == trans[j]:
            arr.append(i)
            arr.append(j)
            print(i, j)
arr = list(set(arr))
print(arr)
to_result = []
for i in range(0, len(string)):
    to_result.append(string[i])
print(to_result)
for i in range(0, arr.__len__()):
    to_result[arr[i]] = 'del'
while 'del' in to_result:
    to_result.remove('del')
print(to_result)
if not string:
    result = ''
else:
    result = to_result[0]
print('result = ', result)
