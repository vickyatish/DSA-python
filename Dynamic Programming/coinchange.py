def coin_change(coins, amount):
    """
    coins: List[int] - denominations available
    amount: int - target amount
    return: int - minimum number of coins to make the amount, or -1 if not possible
    """
    # TODO: implement DP solution
    dp = [amount] * (amount+1)
    dp[0] = 0
    for i in range(1, amount+1):
        for c in coins:
            if c<=i:
                dp[i] = min(dp[i], 1+dp[i-c])

    return dp[amount] if dp[amount]<=amount else -1


def main():
    # Sample test case
    coins = [1, 2, 5]
    amount = 11
    result = coin_change(coins, amount)
    print(f"Minimum coins needed to make {amount}: {result}")


if __name__ == "__main__":
    main()