import sys
def maxProfit(stocks):
	lowest = sys.maxsize - 1
	profit = 0

	for stock in stocks:
		lowest = min(lowest, stock)
		profit = max(profit, stock - lowest)

	return profit

print(maxProfit([7,1,5,3,6,4]))
