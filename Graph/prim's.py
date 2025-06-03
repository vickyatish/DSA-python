import heapq

def prim(graph, start=0):
    """
    graph: adjacency list, where graph[u] = list of (v, weight)
    start: starting vertex
    Returns total weight of MST and list of edges in MST
    """
    visited = set()
    min_heap = [(0, start, -1)]  # (weight, current_node, parent_node)
    mst_weight = 0
    mst_edges = []

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        mst_weight += weight
        if parent != -1:
            mst_edges.append((parent, node, weight))
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))

    return mst_weight, mst_edges


def main():
    # Example graph as adjacency list
    # Each entry: node -> list of (neighbor, weight)
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }

    mst_weight, mst_edges = prim(graph, start=0)
    print(f"Total weight of MST: {mst_weight}")
    print("Edges in MST:")
    for u, v, w in mst_edges:
        print(f"{u} - {v} (weight {w})")

if __name__ == "__main__":
    main()