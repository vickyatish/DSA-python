def subset_sum(nums, target, index):
    
    if target == 0:
        return True

    if index == len(nums):
        return False

    take = subset_sum(nums, target - nums[index], index+1)
    notTake = subset_sum(nums, target, index+1)

    return bool(take + notTake)

def main():
    test_cases = [
        ([2, 3, 7, 8, 10], 11, True),
        ([1, 2, 3, 4, 5], 9, True),
        ([1, 2, 3], 6, True),
        ([1, 2, 3], 7, False),
        ([5, 3, 2], 0, True),
        ([10, 20, 30], 25, False),
        ([7, 14], 21, True),
        ([], 0, True),
        ([], 5, False),
        ([1, 1, 1, 1, 1], 3, True),
    ]

    passed = 0

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = subset_sum(nums, target, 0)
        is_pass = result == expected
        if is_pass:
            passed += 1
        print(f"Test case {i}: nums={nums}, target={target} => Result: {result} (Expected: {expected}) => {'PASS' if is_pass else 'FAIL'}")

    print(f"\nTotal Passed: {passed}/{len(test_cases)}")

if __name__ == "__main__":
    main()