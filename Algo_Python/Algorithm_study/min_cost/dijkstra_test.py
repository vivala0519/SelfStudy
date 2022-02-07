import sys
from Algorithm_study.min_cost.dijkstra import dijkstra_naive, dijkstra_pq

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
assert dijkstra_naive(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]
assert dijkstra_pq(graph, start) == [1000000000, 0, 2, 3, 1, 2, 4]