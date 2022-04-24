import sys

def dfs(v, num):
  num += 1
  visited[v] = True

  if v == b:
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []
for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(a, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0] - 1)