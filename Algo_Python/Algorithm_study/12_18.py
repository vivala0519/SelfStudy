m = 483595
m = str(m)
print(m[:-1] + m[-1])

cnt = 0
while len(m) > 2:
    m = str(int(m[:-1]) - (2 * int(m[-1])))
    cnt += 1
print(m, cnt)