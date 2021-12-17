balls = 20
tot = 0
i = 1
cnt = 0
while tot <= balls:
    tot += i
    i += 1
    if tot <= balls:
        cnt += 1
    else:
        break
print(cnt)