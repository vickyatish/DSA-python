import heapq

def dijkstra(graph, start):
    """
    graph: dict[int, list[tuple[int, int]]] - adjacency list of (neighbor, weight)
    start: int - starting node
    return: dict[int, int] - shortest distances from start to all other nodes
    """
    #TODO: Implement Dijkstra's algorithm here
    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
                continue
        
        for neighbour, weight in graph[current_node]:
            distance = current_distance + weight

            if distance <  distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))
    
    return distances


def main():
    # Test graph as an adjacency list
    # Each node maps to a list of (neighbor, weight)
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    start_node = 0
    result = dijkstra(graph, start_node)

    print("Shortest distances from node", start_node)
    for node in sorted(result):
        print(f"Node {node}: {result[node]}")


if __name__ == "__main__":
    main()
