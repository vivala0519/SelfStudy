import sys
s = sys.stdin.readline().rstrip()

left = 0
right = len(s) - 1

result = 1
while left < right:
    if s[left] != s[right]:
        print(0)
        result = 0
        break
    left += 1
    right -= 1
if result == 1:
    print(1)