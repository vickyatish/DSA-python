def coin_change_ways(coins, amount):
    
    dp = [0] * (amount+1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]

    return dp[amount]

def main():
    # Sample input
    coins = [1, 2, 5]
    amount = 5
    index = 0

    # Expected output: 4
    # Explanation:
    # Ways to make 5: [1,1,1,1,1], [1,1,1,2], [1,2,2], [5]

    result = coin_change_ways(coins, amount)
    print(f"Number of ways to make {amount} using coins {coins[index:]}: {result}")

if __name__ == "__main__":
    main()