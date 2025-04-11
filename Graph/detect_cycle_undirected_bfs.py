from collections import deque

def BFS(graph, node, parent):

	visited = set()
	queue = deque()
	queue.append((node, parent))

	while queue:

		vertex, parent = queue.popleft()
		visited.add(vertex)

		for neighbor in graph[vertex]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append((neighbor, vertex))
			else:
				if neighbor!=parent:
					return True

	return False

def main():
    # Graph without a cycle
    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    # Graph with a cycle
    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]  # Cycle: 0 → 1 → 2 → 3 → 0
    }

    print("Graph1 has cycle?", BFS(graph1, 0, -1))  # Expected: False
    print("Graph2 has cycle?", BFS(graph2, 0, -1))  # Expected: True

if __name__ == "__main__":
    main()