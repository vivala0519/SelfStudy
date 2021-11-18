n = 3
result = ''
for i in range(n):
    if i != n-1:
        result += '+' * n + '\n'
    else:
        result += '+' * n
print(result)