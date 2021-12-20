n = 1

tot, x = 0, 0
while tot < n:
    if tot + pow(x + 1, 2) >= n:
        break
    else:
        x += 1
        tot += pow(x, 2)
print(tot, x)