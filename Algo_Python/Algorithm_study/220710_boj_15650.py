def dfs(arr, idx):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            arr.append(temp[i])
            dfs(arr, i+1)
            visited[i] = False
            arr.pop()


N, M = map(int, input().split())
visited = [False for _ in range(N)]
temp = [i for i in range(1, N+1)]
dfs([], 0)