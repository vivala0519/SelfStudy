from functools import reduce

n = 4

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)

count = 0
while len(str(n)) != 1:
    arr = []
    for i in range(len(str(n))):
        arr.append(int(str(n)[i]))
    n = multiply(arr)
    count += 1
    print(n)
print(count)