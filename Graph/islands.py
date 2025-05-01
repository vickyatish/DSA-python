from collections import deque

def count_islands_bfs(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0
    
    def bfs(r, c):
        # Initialize queue and mark starting cell as visited
        queue = deque([(r, c)])
        visited.add((r, c))
        
        # Directions for the four adjacent cells (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            # Get the current cell
            curr_r, curr_c = queue.popleft()
            
            # Check all four adjacent cells
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                # Check if the neighbor is within bounds, is land, and unvisited
                if (0 <= nr < rows and 
                    0 <= nc < cols and 
                    grid[nr][nc] == 1 and 
                    (nr, nc) not in visited):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
    
    # Iterate through the grid to find unvisited land cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                bfs(r, c)
                islands += 1
    
    return islands

def count_islands_dfs(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    islands = 0
    
    def dfs(r, c):
        # Mark current cell as visited
        visited.add((r, c))
        
        # Directions for the four adjacent cells (up, right, down, left)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Explore all four adjacent cells
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # Check if the neighbor is within bounds, is land, and unvisited
            if (0 <= nr < rows and 
                0 <= nc < cols and 
                grid[nr][nc] == 1 and 
                (nr, nc) not in visited):
                dfs(nr, nc)
    
    # Iterate through the grid to find unvisited land cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                dfs(r, c)
                islands += 1
    
    return islands

def main():
    # Sample island grid (1 = land, 0 = water)
    sample_grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
    bfs_result = count_islands_bfs(sample_grid)
    dfs_result = count_islands_dfs(sample_grid)
    print(f"Number of islands (BFS): {bfs_result}")
    print(f"Number of islands (DFS): {dfs_result}")

if __name__ == "__main__":
    main()