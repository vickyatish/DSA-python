def dfs(adj_list, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=' ')

    for node in adj_list.get(start, []):
        if node not in visited:
            dfs(adj_list, node, visited)

def main():
    adj_list = {
        0: [1, 2],
        1: [3],
        2: [4],
        3: [],
        4: [0]
    }
    dfs(adj_list, 0)

if __name__ == '__main__':
    main()