import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    arr = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    for i in range(1, k + 1):
        temp = []
        for j in range(n):
            temp.append(sum(arr[i-1][:j+1]))
        arr.append(temp)
    print(arr[k][n-1])