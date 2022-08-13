import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr1 = [1] * N
arr2 = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and arr1[i] <= arr1[j]:
            arr1[i] = arr1[j] + 1

for i in range(N - 1, -1, -1):
    for j in range(i, N):
        if A[i] > A[j] and arr2[i] <= arr2[j]:
            arr2[i] = arr2[j] + 1

for i in range(N):
    arr1[i] = arr1[i] + arr2[i] - 1

print(max(arr1))