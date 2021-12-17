n = 21
result = ''
tn = n
for i in range(1, n + 1):
    for j in range(n, 0, -1):
        temp = (' ' * i + (str(i)[-1:] + ' ') * j)[:-1]
        # print(temp)
        if tn == j:
            result += temp + '\n'
    tn = tn - 1
print(result[:-1])


' 1 1 1 1 1 1 1 \n  2 2 2 2 2 2 \n   3 3 3 3 3 \n    4 4 4 4 \n     5 5 5 \n      6 6 \n       7'
' 1 1 1 1 1 1 1\n  2 2 2 2 2 2\n   3 3 3 3 3\n    4 4 4 4\n     5 5 5\n      6 6\n       7'