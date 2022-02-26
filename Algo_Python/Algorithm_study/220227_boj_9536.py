n = int(input())
real_result = []
for _ in range(n):
    s = input().split(' ')
    animal = []
    result = []
    while True:
        x = input()
        if x == 'what does the fox say?':
            break
        animal.append(x.split(' goes ')[1])
    for i in s:
        if i not in animal:
            result.append(i)
    real_result.append(' '.join(result))
for i in real_result:
    print(i)