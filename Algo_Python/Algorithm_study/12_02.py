array = [9, 5, 10, 2, 24, -1, -48]
mul = []
for i in range(len(array)):
    try:
        mul.append(array[i] * array[i+1])
    except:
        pass
print(max(mul))