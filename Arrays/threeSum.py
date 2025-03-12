def threeSum(arr, target):

	Hashset = set()

	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if target - arr[i] - arr[j] in Hashset:
				print(arr[i], arr[j], target-arr[i]-arr[j])
				return True
		Hashset.add(arr[i])

	return False

def threeSumZero(arr):

	answers = set()

	for i in range(len(arr)):
		Hashset = set()
		for j in range(i+1, len(arr)):
			if -(arr[i]+arr[j]) in Hashset:
				answers.add(tuple(sorted([arr[i], arr[j], -(arr[i]+arr[j])])))
			else:
				Hashset.add(arr[j])

	return answers

arr = [-2,1,2,3,4,5,-3,6,7,8]
target = 10

print(threeSum(arr, target))

print(threeSumZero(arr))