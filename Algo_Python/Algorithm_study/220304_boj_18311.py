N, K = 5, 28
arr = [0, 7, 4, 2, 4, 5]

dic = {}
total = 0
for i in range(1, N + 1):
    total += arr[i]
    dic[i] = [arr[i], sum(arr[:i+1])]
print(dic)