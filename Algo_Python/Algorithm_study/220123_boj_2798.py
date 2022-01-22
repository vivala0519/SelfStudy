import sys
temp = sys.stdin.readline().rstrip().split(' ')
n, m = int(temp[0]), int(temp[1])
arr = sys.stdin.readline().rstrip().split(' ')
arr = list(map(int, arr))

max_num = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            temp = arr[i] + arr[j] + arr[k]
            if temp == m:
                max_num = m
                break
            elif temp < m and temp > max_num:
                max_num = temp
            elif temp > m and temp < max_num:
                max_num = temp
            else:
                continue
print(max_num)

