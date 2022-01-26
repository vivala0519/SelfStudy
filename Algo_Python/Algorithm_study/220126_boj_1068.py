import sys
from collections import deque, defaultdict
temp = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
target = int(sys.stdin.readline().rstrip())

edges = defaultdict(list)
for i in range(len(arr)):
    if arr[i] == -1:
        root = i
    else:
        edges[arr[i]].append(i)
print(edges)

cnt = 0
def dfs(node):
    global cnt, target
    if len(edges[node]) == 0:
        cnt += 1
        return
    else:
        for i in edges[node]:
            if i == target and len(edges[node]) == 1:
                cnt += 1
            elif i == target:
                continue
            else:
                dfs(i)

if target == root:
    print(0)
else:
    dfs(root)
    print(cnt)


# print(arr)
# edges = defaultdict(list)
# q = deque()
# q.append(arr.index(-1))
# print(q)
# for i in range(0, len(arr)):
#     if arr[i] != -1:
#         edges[arr[i]].append(i)
# print(edges)
# while q:
#     now = q.popleft()
#     if now == target:
#         del edges[now]
#         break
#     for kid in edges[now]:
#         if kid == target:
#             edges[now].remove(kid)
#             break
#         q.append(kid)
#
# print(edges, len(edges))
# if len(edges) == 0:
#     print(0)
# else:
#     q.append(arr.index(-1))
#     cnt = 0
#     while q:
#         now = q.popleft()
#         for kid in edges[now]:
#             if not edges[kid]:
#                 cnt += 1
#             q.append(kid)
#     print(edges, len(edges))
#     if len(edges) == 1:
#         print(1)
#     else:
#         print(cnt)
