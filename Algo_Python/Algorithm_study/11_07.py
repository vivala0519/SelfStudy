s = 'ooxXm'
os = 0
xs = 0
for i in range(len(s)):
    if s[i] == 'o' or s[i] == 'O':
        os += 1
    elif s[i] == 'x' or s[i] == 'X':
        xs += 1
print(os, xs)
if os == xs:
    print('true')
else:
    print('false')