def twoSum(arr, target):

	hashmap = set()

	for a in arr:
		if target-a in hashmap:
			return [target-a, a]
		else:
			hashmap.add(a)

result = twoSum([1,2,3,4,5], 7)
print(result)