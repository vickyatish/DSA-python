def reverseWords(arr):

	arr = arr.split()

	left = 0
	right = len(arr)-1

	while left<=right:
		arr[left], arr[right] = arr[right], arr[left]
		left+=1
		right-=1

	st = ''
	for a in arr:
		st+=str(a)
		if 

	print(st)

reverseWords('hello world')