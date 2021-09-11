import numpy

n = 12
arr = []
for i in range(1, n+1):
    arr.append(i)
length = len(arr)
while length != 1:
    print(length)
    sieve = [True] * (length+1)
    for i in range(2, int(length ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, length+1, i):
                sieve[j] = False
    c = min([i for i in range(2, (length+1)) if sieve[i]])
    print(c)
    result = [arr[i * c:(i + 1) * c] for i in range((len(arr) + c - 1) // c)]
    print('result : ', result)

    wer = []
    for i in range(0, c):
        temp = []
        wer.append(temp)
    print(wer)
    for i in range(0, c):
        for j in range(0, result.__len__()):
            wer[i].append(result[j][i])
    print(wer)
    arr = wer
    length = arr[0].__len__()
    print(arr)



# for j in sdf:
#     for i in range(0, c):
#         wer[i].append(j)
# print(wer)