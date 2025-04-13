def dfs(node, adj, vis, pathvis):

	vis[node] = 1
	pathvis[node] = 1


	for neighbor in adj[node]:
		
		if not vis[neighbor]:
			if dfs(neighbor, adj, vis, pathvis):
				return True

		elif pathvis[neighbor]:
			return True


	pathvis[node] = 0
	return False

def is_cyclic(n, adj):
    vis = [0] * n
    pathvis = [0] * n

    for node in range(n):
        if not vis[node]:
            if dfs(node, adj, vis, pathvis):
                return True
    return False


# Example usage
if __name__ == "__main__":
    # Number of nodes
    n = 4
    # Adjacency list (Directed graph)
    adj = [
        [1],    # Node 0 -> 1
        [2],    # Node 1 -> 2
        [3],    # Node 2 -> 3
        [1]     # Node 3 -> 1 (creates a cycle)
    ]

    if is_cyclic(n, adj):
        print("Cycle detected")
    else:
        print("No cycle detected")