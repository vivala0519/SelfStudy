dna = 'GCAT'
dna = list(dna)
print(dna)
for i in range(len(dna)):
    if dna[i] == 'T':
        dna[i] = 'U'
dna = ''.join(dna)
print(dna)