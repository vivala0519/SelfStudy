import sys

INF = 10 ** 11

def bf(start):
    dist[start] = 0

    for i in range(N):
        for j in range(1, N + 1):
            for next, cost in graph[j]:
                if dist[next] > dist[j] + cost:
                    dist[next] = dist[j] + cost

                    if i == N - 1:
                        return True
    return False


if __name__ == '__main__':
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split())
        dist = [INF for _ in range(N+1)]
        graph = [[] for _ in range(N+1)]

        for _ in range(M):
            S, E, T = map(int, sys.stdin.readline().split())
            graph[S].append((E, T))
            graph[E].append((S, T))

        for _ in range(W):
            S, E, T = map(int, sys.stdin.readline().split())
            graph[S].append((E, -T))

        if bf(1):
            print('YES')
        else:
            print('NO')