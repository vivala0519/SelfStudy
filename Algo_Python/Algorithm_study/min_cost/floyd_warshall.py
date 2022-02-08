inf = int(1e9)

def floyd_warshall(graph):
    n = len(graph)
    dist = [[inf] * (n + 1) for _ in range(n + 1)]

    for idx in range(1, n + 1):
        dist[idx][idx] = 0

    for start, adjs in graph.items():
        for adj, d in adjs:
            dist[start][adj] = d
    
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])
    
    return dist