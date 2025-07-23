def change(amount, coins):
    """
    Returns the number of combinations that make up the given amount using the coins.
    
    Parameters:
    - amount (int): the target amount
    - coins (List[int]): available coin denominations

    Returns:
    - int: number of unique combinations to form the amount
    """
    # TODO: Implement the solution here
    def dfs(index, current_amount):
        if current_amount == amount:
            return 1
        if index==len(coins) or current_amount>amount:
            return 0
        
        return dfs(index, current_amount+coins[index]) + dfs(index+1, current_amount)
    
    return dfs(0,0)


def main():
    # Sample test case
    amount = 5
    coins = [1, 2, 3]
    result = change(amount, coins)
    print(f"Number of combinations to make {amount} using {coins} is: {result}")


if __name__ == "__main__":
    main()