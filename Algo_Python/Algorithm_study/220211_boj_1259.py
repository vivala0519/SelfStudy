import sys
while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    left = 0
    right = len(s) - 1
    for _ in range(len(s) // 2):
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            print('no')
            break
    if left >= len(s) // 2:
        print('yes')