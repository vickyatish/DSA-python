from collections import deque

def bfs(n, adj):

	indigree = [0]*n 

	for i in range(n):
		for neighbor in adj[i]:
			indigree[neighbor] += 1

	queue = deque([u for u in range(n) if indigree[u]==0])
	topo = []

	while queue:
		node = queue.popleft()
		topo.append(node)

		for neighbor in adj[node]:
			indigree[neighbor] -= 1
			if indigree[neighbor] == 0:
				topo.append(neighbor)

	return topo

# 👇 Sample Main Function
def main():
    n = 6
    adj = [[] for _ in range(n)]
    adj[5].extend([0, 2])
    adj[4].extend([0, 1])
    adj[2].append(3)
    adj[3].append(1)

    result = bfs(n, adj)
    print("Topological Order:", result)

main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              