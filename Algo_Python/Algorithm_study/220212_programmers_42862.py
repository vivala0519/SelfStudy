n, lost, reserve = 5, [2, 4], [1, 3, 5]

real = []
reserve = list(set(reserve) - set(lost))
lost = list(set(lost) - set(reserve))
print(reserve, lost)


for i in reserve:
    if i - 1 in lost:
        lost.remove(i - 1)
    elif i + 1 in lost:
        lost.remove(i + 1)
print(n - len(lost))