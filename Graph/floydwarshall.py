def floydWarshall(graph):
    V = len(graph)
    dist = graph.copy()

    for k in range(V):
        for j in range(V):
            for i in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

INF = float('inf')
graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

shortest_paths = floydWarshall(graph)
for row in shortest_paths:
    print(row)