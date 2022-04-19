import sys

# S = 'lovey0uS2'
# K = 'veS'
S = sys.stdin.readline().rstrip()
K = sys.stdin.readline().rstrip()

newS = ''
for i in S:
    if i.isalpha():
        newS += i
if K in newS:
    print(1)
else:
    print(0)