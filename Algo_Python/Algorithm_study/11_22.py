n, d = 5750, 0
arr = []
for k in range(n+1):
    if str(d) in str(k * k):
        arr.append(str(k * k).count(str(d)))
print(sum(arr))