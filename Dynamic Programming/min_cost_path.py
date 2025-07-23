def min_cost_path(grid, n, m):

    dp = [[0]*m for _ in range(n)]

    dp[0][0] = grid[0][0]

    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = grid[i][j] + min(dp[i][j-1], dp[i-1][j])

    return dp[n-1][m-1]

def main():
    # Sample test case (you can modify this)
    T = 1
    test_cases = [
        {
            'n': 10,
            'm': 10,
            'grid' : [
                        [1, 100, 1,   1,   100, 1,   1,   100, 1,   1],
                        [1,   1, 100, 1,   1,   100, 1,   1,   100, 1],
                        [100, 1, 1,   100, 1,   1,   100, 1,   1,   100],
                        [1,   100, 1, 1,   100, 1,   1,   100, 1,   1],
                        [1,   1,   100, 1, 1,   100, 1,   1,   100, 1],
                        [100, 1, 1,   100, 1, 1,   100, 1,   1,   100],
                        [1,   100, 1, 1,   100, 1, 1,   100, 1,   1],
                        [1,   1,   100, 1, 1,   100, 1,   1,   100, 1],
                        [100, 1, 1,   100, 1, 1,   100, 1,   1,   100],
                        [1,   100, 1, 1,   100, 1, 1,   100, 1,   1],
                    ]
        }
    ]
    
    for case in test_cases:
        n = case['n']
        m = case['m']
        grid = case['grid']
        result = min_cost_path(grid, n, m)
        print(f"Minimum path cost: {result}")


if __name__ == "__main__":
    main()
