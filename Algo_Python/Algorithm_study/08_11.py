n = 5050


if n == 1:
    location = 0
else:
    square = str(n * n)
    print(square)
    location = int(square.__len__() / 2)
    print(location)
    result = int(square[:location]) + int(square[location:])
    if n != result:
        location = -1
print(result)
print(location)