from itertools import groupby

chars = 'bbbaaabaaaa'
res = max([len(list(g)) for k, g in groupby(chars)])
char_list = []
length = []
for k, g in groupby(chars):
    char_list.append(k)
    length.append(len(list(g)))
max_num = max(length)
for_char = length.index(max_num)
result = char_list[for_char], max_num
print(result)
