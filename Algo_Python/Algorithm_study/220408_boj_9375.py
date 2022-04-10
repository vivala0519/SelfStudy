# clothes = [['hat', 'headgear'], ['sunglasses', 'eyewear'], ['turban', 'headgear']]
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    clothes = []
    for _ in range(n):
        clothes.append(sys.stdin.readline().rstrip().split())

    dic = {}
    for item in clothes:
        if item[1] not in dic:
            dic[item[1]] = [item[0]]
        else:
            dic[item[1]].append(item[0])
    # print(dic)

    total = 1
    for item in dic.keys():
        total *= (len(dic[item]) + 1)

    print(total-1)