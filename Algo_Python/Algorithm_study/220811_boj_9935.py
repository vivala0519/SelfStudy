import sys

S1 = sys.stdin.readline().rstrip()
S2 = sys.stdin.readline().rstrip()
stack = []

for i in S1:
    stack.append(i)
    if i == stack[-1] and ''.join(stack[-len(S2):]) == S2:
        del stack[-len(S2):]

result = ''.join(stack)
if result == '':
    print('FRULA')
else:
    print(result)