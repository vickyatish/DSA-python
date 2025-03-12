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


def threeSumTwoPointers(arr):
    answers = set()
    arr.sort()

    i = 0
    while i < len(arr) - 2:  # We need at least 3 elements
        if i > 0 and arr[i] == arr[i - 1]:
            i += 1  # Skip duplicate values of i to avoid duplicate triplets
            continue
        
        j, k = i + 1, len(arr) - 1  # Initialize two pointers

        while j < k:
            summ = arr[i] + arr[j] + arr[k]

            if summ < 0:
                j += 1  # Move j to the right to increase the sum
            elif summ > 0:
                k -= 1  # Move k to the left to decrease the sum
            else:
                # Found a triplet
                answers.add((arr[i], arr[j], arr[k]))

                # Skip duplicates for j
                while j < k and arr[j] == arr[j + 1]:
                    j += 1

                # Skip duplicates for k
                while j < k and arr[k] == arr[k - 1]:
                    k -= 1

                # Move both pointers to the next potential distinct values
                j += 1
                k -= 1

        i += 1  # Move i to the next element to continue searching

    return answers

arr = [-2,1,2,3,4,5,-3,6,7,8]
target = 10

print(threeSum(arr, target))

print(threeSumZero(arr))

print(threeSumTwoPointers(arr))