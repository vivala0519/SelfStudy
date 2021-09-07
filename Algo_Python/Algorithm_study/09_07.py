lst = [1, 1, 5, 6, 9, 16, 27]
n = 4
count = 0
for i in range(0, lst.__len__()):
    for j in range(i+1, lst.__len__()):
        if i == j:
            pass
        else:
            print(lst[i], lst[j], lst[i] - lst[j])
            if abs(lst[i] - lst[j]) == n:
                count += 1
                print(lst[i] - lst[j])
print(count)