import sys

N, A, D = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

for i in range(N):
    if arr[i] == A + (result * D):
        result += 1
        
print(result)