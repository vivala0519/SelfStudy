# s = 'So when I die (the [first] I will see in (heaven) is a score list).'
# s = '[ first in ] ( first out ).'
# s = 'Half Moon tonight (At least it is better than no Moon at all].'
# s = 'A rope may form )( a trail in a maze.'
# s = 'Help( I[m being held prisoner in a fortune cookie factory)].'
# s = '([ (([( [ ] ) ( ) (( ))] )) ]).'
# s = ' .'
import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == ".":
        break

    stack = []
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print('no')
    else:
        print('yes')
