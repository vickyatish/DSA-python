def subset_sum(nums, target):


    n=len(nums)
    dp = [[False] * (target+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                # Include or exclude current number
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                # Can't include, so just exclude
                dp[i][j] = dp[i - 1][j]
    

    return dp[n][target]


def main():
    test_cases = [
        ([3, 34, 4, 12, 5, 2], 9),     # True: subset [4, 5] or [3, 4, 2]
        ([1, 2, 3, 7], 6),             # True: subset [1, 2, 3]
        ([1, 2, 7, 1, 5], 10),         # True: subset [2, 7, 1]
        ([1, 3, 5, 9], 14),            # True: [5, 9]
        ([2, 4, 6, 8], 5),             # False: no subset sums to 5
    ]

    for nums, target in test_cases:
        result = subset_sum(nums, target)
        print(f"Subset sum of {target} in {nums} → {result}")

if __name__ == "__main__":
    main()