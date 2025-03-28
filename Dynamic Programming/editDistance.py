def editDistance(s1, s2, i, j):
	if i<0:
		return j+1
	if j<0:
		return i+1

	if s1[i]==s2[j]:
		return editDistance(s1, s2, i-1, j-1)
	else:
		return 1+min(editDistance(s1,s2,i-1,j),min(editDistance(s1,s2,i,j-1),editDistance(s1,s2,i-1,j-1)))


s1 = "horse"
s2 = "ros"

print("The minimum number of operations required is:", editDistance(s1, s2, len(s1)-1, len(s2)-1))