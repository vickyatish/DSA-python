def subsetSum(arr, target):

	n = len(arr)
	dp = [[False for i in range(target+1)] for _ in range(n+1)]

	for i in range(n+1):
		dp[i][0] = True

	for i in range(1, n + 1):
		for j in range(1, target + 1):
			if j < arr[i-1]:
				dp[i][j] = dp[i-1][j]
			else:
				dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]

	if not dp[n][target]:
		print(f"No subset with sum {target} exists")
		return
    
    # Backtrack to find the subset
	subset = []
	i, j = n, target
	while i > 0 and j > 0:
		if dp[i-1][j]:
			i -= 1  # Exclude arr[i-1]
		else:
			subset.append(arr[i-1])  # Include arr[i-1]
			j -= arr[i-1]
			i -= 1
			
	print(f"Subset with sum {target}: {subset}")
def main():
	arr = [3, 34, 4, 12, 5, 2]
	target = 9
	subsetSum(arr, target)

if __name__ == '__main__':
	main()