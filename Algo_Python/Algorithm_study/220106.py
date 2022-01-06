wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
                    {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
                    {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
                    {'size': "small", 'clatters': "yes", 'weight': "light"}]

arr = []
for i in range(len(presents)):
    for j in range(len(wishlist)):
        if presents[i]['size'] == wishlist[j]['size'] and presents[i]['clatters'] == wishlist[j]['clatters'] and presents[i]['weight'] == wishlist[j]['weight']:
            arr.append(wishlist[j]['name'])
arr = list(set(arr))
print(arr)
