character = '10 5 2'
# 체 공 방
monster = ["Knight 3 10 10 3", "Wizard 5 10 15 1", "Beginner 1 1 15 1"]
# 이름 경 체 공 방

result = []
character = character.split(' ')
for i in range(len(character)):
    character[i] = int(character[i])
print(character)
for i in range(len(monster)):
    monster[i] = monster[i].split(' ')
print(monster)
for i in monster:
    to_damage = character[1] - int(i[4])
    from_damage = int(i[3]) - character[2]
    print(to_damage, from_damage)
    if int(i[2]) < to_damage:
        result.append(int(i[1]))
    else:
        if character[0] < from_damage:
            result.append(0)
        else:
            result.append(int(i[1]) / (int(i[2]) / to_damage))
print(result)

result = result.index(max(result))
result = monster[result][0]
print(result)



# daily algo


n, m = 7, 4
print(n * m -1)