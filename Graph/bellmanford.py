# bellman_ford.py

from typing import Any, Dict, List, Tuple, Union

def bellman_ford(
    nodes: List[Any], 
    edges: List[Tuple[Union[int, float], Union[int, float], Union[int, float]]],
    src: Any
) -> Tuple[Dict[Any, float], bool]:
    """
    Computes shortest-path distances from src to all other nodes using the Bellman–Ford algorithm.
    Detects if there is a negative-weight cycle reachable from src.
    
    Args:
        nodes: A list of all vertices in the graph (can be ints, strings, etc.).
        edges: A list of tuples (u, v, w) representing a directed edge u->v with weight w.
        src:   The source vertex from which to measure distances.
    
    Returns:
        dist:               A dict mapping each node to its shortest-path distance from src.
                            If a node is unreachable, its distance remains float('inf').
        has_negative_cycle: True if a negative-weight cycle is detected (reachable from src), else False.
    """
    distances: Dict[Any, float] = {node: float('inf') for node in nodes}
    distances[src] = 0.0

    # Relax edges |V| - 1 times
    for _ in range(len(nodes) - 1):
        updated = False
        for (u, v, w) in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                updated = True
        if not updated:
            break  # No changes this iteration, we can stop early

    # Check for negative-weight cycles
    has_negative_cycle = False
    for (u, v, w) in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            has_negative_cycle = True
            break

    return distances, has_negative_cycle


if __name__ == "__main__":
    # Example usage:

    # Define a graph with 5 nodes: 0, 1, 2, 3, 4
    nodes = [0, 1, 2, 3, 4]

    # Define edges as (u, v, w):
    #   0 -> 1 (weight 6)
    #   0 -> 2 (weight 7)
    #   1 -> 2 (weight 8)
    #   1 -> 3 (weight 5)
    #   1 -> 4 (weight -4)
    #   2 -> 3 (weight -3)
    #   2 -> 4 (weight 9)
    #   3 -> 1 (weight -2)
    #   4 -> 0 (weight 2)
    #   4 -> 3 (weight 7)
    edges = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 0, 2),
        (4, 3, 7),
    ]

    source = 0
    distances, negative_cycle = bellman_ford(nodes, edges, source)

    if negative_cycle:
        print("Graph contains a negative-weight cycle reachable from source.")
    else:
        print(f"Shortest distances from node {source}:")
        for node in nodes:
            d = distances[node]
            if d == float('inf'):
                print(f"  {node}: unreachable")
            else:
                print(f"  {node}: {d}")
