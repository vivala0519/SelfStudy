word = 'EIO'

dic = ['A', 'E', 'I', 'O', 'U']

dic_list = []
for i in range(0, dic.__len__()):
    char = ''
    for j in range(1, 6):
        char = dic[i] * j
        dic_list.append(char)
        if char.__len__() == 5:
            for k in range(1, 5):
                char = char[0:4]
                char += dic[k]
                dic_list.append(char)
    for j in range(1, 5):
        char = char[0:3]
        char += dic[j]
        dic_list.append(char)
        for k in range(0, 5):
            char = char[0:4]
            char += dic[k]
            dic_list.append(char)
    for j in range(1, 5):
        char = char[0:2]
        char += dic[j]
        dic_list.append(char)
        for k in range(0, 5):
            char = char[0:3]
            char += dic[k]
            dic_list.append(char)
            for l in range(0, 5):
                char = char[0:4]
                char += dic[l]
                dic_list.append(char)
    for j in range(1, 5):
        char = char[0:1]
        char += dic[j]
        dic_list.append(char)
        for k in range(0, 5):
            char = char[0:2]
            char += dic[k]
            dic_list.append(char)
            for l in range(0, 5):
                char = char[0:3]
                char += dic[l]
                dic_list.append(char)
                for m in range(0, 5):
                    char = char[0:4]
                    char += dic[m]
                    dic_list.append(char)
print(dic_list)
print(dic_list.index(word) + 1)

from itertools import product
dic_list = []
for i in range(1, 6):
    temp = list(map(''.join, product(dic, repeat=i)))
    dic_list.extend(temp)
dic_list.sort()
print(dic_list)
