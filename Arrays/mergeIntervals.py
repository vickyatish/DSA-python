def mergeIntervals(arr):

	n = len(arr)
	
	ans = []

	for i in range(n):

		start, end = arr[i][0], arr[i][1]

		if ans and end <= ans[-1][1]:
			continue

		for j in range(i+1, n):

			if arr[j][0] < end:
				end = max(end, arr[j][1])
			else:
				break


		ans.append([start,end])

	return ans

def mergeIntervals2(arr):

	n = len(arr)

	ans = []

	for i in range(n):

		if not ans or arr[i][0] > ans[-1][1]:
			ans.append(arr[i])

		else:
			ans[-1][1] = max(arr[i][1], ans[-1][1])

	return ans

if __name__ == '__main__':
	
	arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
	ans = mergeIntervals2(arr)
	print("The merged intervals are:")
	for it in ans:
		print(f"[{it[0]}, {it[1]}]", end=" ")
		print()