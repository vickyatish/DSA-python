visited = set()

def DFS(graph, node, parent):
	visited.add(node)

	for neighbor in graph[node]:
		if neighbor not in visited:
			visited.add(neighbor)
			if DFS(graph, neighbor, node):
				return True
		else:
			if neighbor!=parent:
				return True

	return False

def main():
    global visited

    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    visited = set()
    print("Graph1 has cycle (DFS)?", DFS(graph1, 0, -1))  # Expected: False

    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]
    }

    visited = set()
    print("Graph2 has cycle (DFS)?", DFS(graph2, 0, -1))  # Expected: True

if __name__ == "__main__":
    main()