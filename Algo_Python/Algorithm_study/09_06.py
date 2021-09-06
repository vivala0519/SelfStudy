weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]
rate = []
heavier_win_count = []
for i in head2head:
    win_count = 0
    lose_count = 0
    for j in range(0, weights.__len__()):
        if i[j] == 'N':
            pass
        elif i[j] == 'W':
            win_count += 1
        else:
            lose_count += 1
    try:
        rate.append(win_count / (win_count + lose_count))
    except:
        rate.append(0)
for i in range(0, weights.__len__()):
    count = 0
    for j in range(0, weights.__len__()):
        if weights[i] < weights[j] and head2head[i][j] == 'W':
            count += 1
        else:
            pass
    heavier_win_count.append(count)

players = []
for i in range(0, weights.__len__()):
    dic = {}
    dic['number'] = i + 1
    dic['weight'] = weights[i]
    dic['rate'] = rate[i]
    dic['heavier_win'] = heavier_win_count[i]
    players.append(dic)

# print(rate)
# print(heavier_win_count)
# print(players)
players = sorted(players, key=(lambda x: x['weight']), reverse=True)
# print(players)
players = sorted(players, key=(lambda x: x['heavier_win']), reverse=True)
# print(players)
players = sorted(players, key=(lambda x: x['rate']), reverse=True)
print(players)
result = []
for i in range(0, weights.__len__()):
    result.append(players[i]['number'])
print(result)