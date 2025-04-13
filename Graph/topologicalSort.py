def dfs(node, adj, vis, st):

	vis[node] = 1

	for neighbor in adj[node]:
		if not vis[neighbor]:
			dfs(neighbor, adj, vis, st)
	st.append(node)


def main():
    # Number of nodes
    n = 16

    # Adjacency list (Directed edges)
    adj = [[] for _ in range(n)]
    
    adj[1].append(2)
    adj[1].append(3)
    adj[2].append(4)
    adj[2].append(5)
    adj[3].append(6)
    adj[3].append(7)
    adj[4].append(8)
    adj[4].append(9)
    adj[5].append(10)
    adj[5].append(11)
    adj[6].append(12)
    adj[6].append(13)
    adj[7].append(14)
    adj[7].append(15)

    vis = [0] * n
    st = []

    for i in range(n):
        if not vis[i]:
            dfs(i, adj, vis, st)

    # Reverse stack to get topological ordering
    st.reverse()
    print("Topological Sort:", st)

if __name__ == "__main__":
    main()