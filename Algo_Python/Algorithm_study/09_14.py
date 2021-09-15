s = 'supercalifragilisticexpialidocious'
part_length = 3

arr = []
result = ''
for i in range(0, len(s), part_length):
    result += s[i:i+part_length] + ' '
print(result.lstrip())

def split_in_parts(s, part_length):
    result = ''
    for i in range(0, len(s), part_length):
        result += s[i:i+part_length] + ' '
    return result.rstrip()