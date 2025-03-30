from collections import deque

def BFS(graph, node):

	visited = set()
	queue = deque([node])
	visited.add(node)
	print(node)

	while queue:

		vertex = queue.popleft()

		for neighbour in graph[vertex]:
			if neighbour not in visited:
				visited.add(neighbour)
				print(neighbour)
				queue.append(neighbour)




if __name__ == '__main__':

	graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
	}

	BFS(graph, 'A')