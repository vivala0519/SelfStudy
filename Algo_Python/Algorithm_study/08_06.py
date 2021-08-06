s = 'kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu'
length = len(s)
print(length)
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
count = 0
for i in range(0, length):
    for j in range(0, arr.__len__()):
        if arr[j] == s[i]:
            count += 1
print(count)
error = length - count
print(error)
result = str(error) + '/' + str(length)
print(result)