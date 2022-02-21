import sys
alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_lower = 'abcdefghijklmnopqrstuvwxyz'

s = sys.stdin.readline().rstrip()

result = []
for i in s:
    if i.isalpha():
        if i.isupper():
            x = alpha_upper.index(i) + 13
            if x >= 26:
                x -= 26
            result.append(alpha_upper[x])
        else:
            x = alpha_lower.index(i) + 13
            if x >= 26:
                x -= 26
            result.append(alpha_lower[x])
    else:
        result.append(i)
print(''.join(result))
