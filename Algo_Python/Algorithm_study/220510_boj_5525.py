import sys


# S = 'OOIOIOIOIIOII'
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

temp = 'I'
for i in range(N):
    temp += 'O'
    temp += 'I'


cnt = 0
for i in range(len(S)):
    if S[i:i+len(temp)] == temp:
        cnt += 1
print(cnt) 

cnt = 0
stack = []
for i in range(M):
    if S[i] == 'O':
        continue
    else:
        stack.append(i)

result = 0
for i in range(1, len(stack)):
    if stack[i] - stack[i - 1] == 2:
        cnt += 1
    else:
        cnt = 0
    
    if cnt >= N:
        result += 1

print(result)