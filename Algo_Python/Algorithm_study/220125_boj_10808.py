import sys
temp = sys.stdin.readline().rstrip()
alpha = 'abcdefghijklmnopqrstuvwxyz'

result = []
for i in range(len(alpha)):
    if alpha[i] in temp:
        result.append(str(temp.count(alpha[i])))
    else:
        result.append('0')
print(' '.join(result))