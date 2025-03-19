def maxProd(arr):

	maxx = 0

	n = len(arr)
	for i in range(n):
		prod = 1
		for j in range(i+1,n):
			prod *= arr[j]
			if prod>maxx:
				maxx = prod 

	return maxx

def maxProdDP(arr):
	n = len(arr)
	dp = arr
	i = 1
	while i<n-1:
		if dp[i]!=0:
			dp[i+1] *= dp[i]
		else:
			dp[i]=1
		print(dp[i],i)
		i+=1

	return dp


def maxProdNZ(arr):
    n = len(arr)
    if n == 0:
        return 0

    max_prod = float('-inf')
    min_prod = float('inf')
    cur_max, cur_min = 1, 1  # Track both max and min product

    for num in arr:
        temp = cur_max  # Store current max before updating
        cur_max = max(num, cur_max * num, cur_min * num)
        cur_min = min(num, temp * num, cur_min * num)

        max_prod = max(max_prod, cur_max)
        min_prod = min(min_prod, cur_min)
 
    return min_prod



arr = [1,2,-3,-4,-5]
print(maxProdNZ(arr))