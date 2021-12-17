electrons = 47
arr = []
i = 1
while electrons > 0:
    electrons = electrons - 2 * (i ** 2)
    if electrons < 0:
        arr.append(2 * (i ** 2) + electrons)
    else:
        arr.append(2 * (i ** 2))
    print(electrons)
    i += 1
print(arr)