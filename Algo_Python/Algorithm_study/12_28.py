gloves = ["red", "green", "blue", "blue", "red", "green", "red", "red", "red"]
arr = list(set(gloves))
dic = {}
count = 0
for i in arr:
    dic.setdefault(i, 0)
print(dic)
for i in gloves:
    if i in dic.keys():
        dic[i] += 1
print(dic)
for i in dic.values():
    count += int(i/2)
print(count)