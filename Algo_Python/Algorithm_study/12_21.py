deck_size = 52
arche = []
left = []
right = []
temp = []
cnt = 1

# for i in range(0, deck_size):
#     arche.append(i)
for i in range(0, int(deck_size/2)):
    left.append(i)
    arche.append(i)
for i in range(int(deck_size/2), deck_size):
    right.append(i)
    arche.append(i)
print('arche = ', arche)
print(left, right)

for i in range(0, int(deck_size / 2)):
    temp.append(left[i])
    temp.append(right[i])
print('temp', temp)
while arche != temp:
    left = []
    right = []
    for i in range(0, int(len(temp)/2)):
        left.append(temp[i])
    for i in range(int(len(temp)/2), len(temp)):
        right.append(temp[i])
    print('left', left, 'right',  right)
    temp = []
    for i in range(0, int(deck_size/2)):
        temp.append(left[i])
        temp.append(right[i])
    print(temp)
    cnt += 1
print(cnt)