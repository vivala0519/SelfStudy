bobs_decisions = ('F', 'M', 'F')
expert_decisions = ('M', 'F', 'M')

score = 0
for i in range(len(bobs_decisions)):
    if bobs_decisions[i] == expert_decisions[i]:
        score += 1
        print('+1')
    elif bobs_decisions[i] == '?' or expert_decisions[i] == '?':
        score += 0.5
        print('+0.5')
    else:
        pass
print(score)