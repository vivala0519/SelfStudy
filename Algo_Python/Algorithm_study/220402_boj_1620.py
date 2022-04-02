import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

pokemon = {}
for i in range(1, N + 1):
    x = sys.stdin.readline().rstrip()
    pokemon[i] = x
    pokemon[x] = i


command = []
for _ in range(M):
    command.append(sys.stdin.readline().rstrip())

for i in command:
    if i.isdigit():
        print(pokemon[int(i)])
    else:
        print(pokemon[i])