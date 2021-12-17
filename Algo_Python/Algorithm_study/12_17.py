array = [6,5,4,3,2,1]
inversions = 0
for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i] > array[j]:
            print(array[i], array[j])
            inversions += 1
print(inversions)