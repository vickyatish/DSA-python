def editDistance(s1, s2, i, j):
	if i<0:
		return j+1
	if j<0:
		return i+1

	if s1[i]==s2[j]:
		return editDistance(s1, s2, i-1, j-1)
	else:
		return 1+min(editDistance(s1,s2,i-1,j),min(editDistance(s1,s2,i,j-1),editDistance(s1,s2,i-1,j-1)))

def editDistanceDP(s1, s2, m, n):

	dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

	for i in range(m+1):
		dp[0][i] = i
	for j in range(n+1):
		dp[j][0] = j

	for i in range(1,n+1):
		for j in range(1,m+1):
			if s1[i-1]==s2[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1+min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))

	print(dp[-1][-1])

s1 = "kitten"
s2 = "sitting"

editDistanceDP(s1, s2, 4, 2)
#print("The minimum number of operations required is:", editDistance(s1, s2, len(s1)-1, len(s2)-1))