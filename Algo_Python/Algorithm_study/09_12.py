seq = [1,2,2,3,3,3,4,3,3,3,2,2,1]

for i in seq:
    if seq.count(i) % 2 == 1:
        result = i
print(result)