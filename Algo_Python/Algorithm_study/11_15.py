dna = 'ATTGC'
arr = []
for i in range(len(dna)):
    if dna[i] == 'A':
        arr.append('T')
    elif dna[i] == 'T':
        arr.append('A')
    elif dna[i] == 'G':
        arr.append('C')
    else:
        arr.append('G')
print(arr)
result = ''.join(arr)
print(result)