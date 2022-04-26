from itertools import combinations

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i,j))
        if graph[i][j] == 2:
            chicken.append((i,j))
chicken_combi = list(combinations(chicken,m))

result = []
for i in chicken_combi:
    total = 0
    for j in house:
        min_arr = []
        for k in i:
            dist = abs(k[0] - j[0]) + abs(k[1] - j[1])
            min_arr.append(dist)
        total += min(min_arr)
    result.append(total)
print(min(result))