a, b = 'old father, old artificer', 'of my soul the uncreated '
count = 0
for i in range(len(a)):
    if a[i] != b[i]:
        print(a[i], b[i])
        count += 1
print(count)