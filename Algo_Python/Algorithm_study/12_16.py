left, right = "!!???!????", "??!!?!!!!!!!"
left_score, right_score = 0, 0
for i in range(len(left)):
    if left[i] == '!':
        left_score += 2
    else:
        left_score += 3
for i in range(len(right)):
    if right[i] == '!':
        right_score += 2
    else:
        right_score += 3
print(left_score, right_score)