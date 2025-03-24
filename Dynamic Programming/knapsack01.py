def knapsack(weights, values, n, W):
	if n==0 or W==0:
		return 0

	if weights[n-1]>W:
		return knapsack(weights, values, n-1, W)

	include = values[n-1] + knapsack(weights, values, n-1, W-weights[n-1])
	exclude = knapsack(weights, values, n-1, W)

	return max(include, exclude)

def knapsackdp(weights, values, n, W):
	dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

	for i in range(1,n+1):
		for w in range(W+1):
			if weights[i-1]<=w:
				dp[i][w] = max(values[i-1]+dp[i-1][w-weights[i-1]], dp[i-1][w])
			else:
				dp[i][w] = dp[i-1][w]

	return dp[n][W]

values = [10, 15, 20]  # Values of items
weights = [2, 3, 4]    # Weights of items
W = 5                  # Knapsack capacity
n = len(values)
print(knapsackdp(weights, values, n, W))  # Output: 25values = [10, 15, 20]  # Values of items