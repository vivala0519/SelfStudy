array = [33,99,100,30,29]

array.sort()
print(array)
print(array[int((len(array)-1)/2)])
if len(array) % 2 == 0:
    print((array[int((len(array)-1)/2)] + array[int((len(array)-1)/2) + 1]) / 2)
else:
    print(array[int((len(array))/2)])