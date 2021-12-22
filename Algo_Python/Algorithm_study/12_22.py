lst = [1, 2, 3, 4, 5]
for i in range(len(lst)):
    if i % 2 == 1:
        lst[i] = lst[i] * 2
print(lst)