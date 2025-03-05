def twoSum(arr, target):

	hashmap = set()

	for a in arr:
		if target-a in hashmap:
			return [target-a, a]
		else:
			hashmap.add(a)

def twoSum2(arr, target):

	left, right = 0, len(arr)-1

	while left<right:
		if arr[left]+arr[right]<target:
			left+=1
		elif arr[left]+arr[right]>target:
			right-=1
		else:
			print ([arr[left], arr[right]])
			left+=1
	return

result = twoSum2([1,2,3,4,5], 7)
print(result)