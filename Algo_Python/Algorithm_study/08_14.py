height = 17
width = 32
length = 11
arr = [height, width, length]
first = max(arr)
arr.remove(first)
second = max(arr)
arr.remove(second)
third = arr[0]
total = first * 2 + second * 2 + third * 4 + 20
print(total)
