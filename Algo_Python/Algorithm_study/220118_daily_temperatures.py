t = [73, 74, 75, 71, 69, 72, 76, 73]
answer = [0] * len(t)
stack = []
for i, cur in enumerate(t):
    while stack and cur > t[stack[-1]]:
        last = stack.pop()
        answer[last] = i - last
    stack.append(i)

print(answer)