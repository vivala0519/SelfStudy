import sys
t = int(sys.stdin.readline().rstrip())

result = []
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split())
    ho = n // h + 1
    layer = n % h
    if layer == 0:
        result.append(h * 100 + ho - 1)
    else:
        result.append(layer * 100 + ho)
for i in result:
    print(i)

