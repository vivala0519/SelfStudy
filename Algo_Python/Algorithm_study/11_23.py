array = [7, 1, 7, 1]
arr = []
for i in range(len(array)):
    try:
        arr.append(abs(array[i] - array[i+1]))
    except:
        pass
print(sum(arr))
