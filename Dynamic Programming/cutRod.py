def maxProfit(n, price):
    
    if n == 0:
        return 0

    answer = float('-inf')
    
    for i in range(n):
        if i + 1 <= n:
            rodPrice = price[i] + maxProfit(n-(i+1), price)
            answer = max(answer, rodPrice)

    return answer


def main():
    # Sample test case
    price = [2, 5, 7, 8]  # prices for lengths 1, 2, 3, 4
    n = 4  # rod length
    result = maxProfit(n, price)
    print("Maximum Profit:", result)


if __name__ == "__main__":
    main()