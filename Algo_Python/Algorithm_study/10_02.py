k = 2
a = [10110, 10102, 10097, 10113, 10123, 10109, 10118, 10119, 10117, 10115, 10101, 10121, 10122]
f = []
for i in a:
    li, j = [], 2
    while j*j <= i:
        if i % j:
            j += 1
        else:
            i /= j
            li.append(j)
    if i > 1:
        li.append(i)
    f.append(len(li))
print(f)
print(sum(i == j == k for i, j in zip(f, f[1:])))