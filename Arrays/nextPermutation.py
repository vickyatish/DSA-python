def nextPermutation(nums):
    n = len(nums)
    ind = -1

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            ind = i
            break
    
    if ind == -1:
        return reversed(nums)
    
    for i in range(n-1, ind, -1):
        if nums[i]>nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break
    
    nums[ind+1:] = reversed(nums[ind+1:])

    return nums

if __name__ == "__main__":
    A = [2, 1, 5, 4, 3, 0, 0]
    ans = nextPermutation(A)

    print("The next permutation is: [", end="")
    for it in ans:
        print(it, end=" ")
    print("]")