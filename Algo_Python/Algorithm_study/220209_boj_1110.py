n = 71

def slice_num(n):
    if n < 10:
        return int(str(n) + str(n))
    temp = int(str(n)[0]) + int(str(n)[1])
    if temp < 10:
        n = str(n)[1] + str(temp)
    else:
        n = str(n)[1] + str(temp)[1]
    return int(n)

first = slice_num(n)
cnt = 1
while first != n:
    first = slice_num(first)
    cnt += 1
print(cnt)
