number = 16
hap = 0
arr = []
for i in range(1, number):
    sam = 3 * i
    oh = 5 * i
    if sam < number:
        print(sam)
        arr.append(sam)
    if oh < number:
        print(oh)
        arr.append(oh)
arr = set(arr)
print(arr)
hap = sum(arr)
print(hap)