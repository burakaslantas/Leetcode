class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        balance = -prices[0]
        profit = 0
        
        #we have only three options: buy, rest, sell
        for i in range(1, len(prices)):
            #decide rest or buy on balance
            balance = max(balance, profit - prices[i])
            #decide rest or sell to make maximum profit
            profit = max(profit, balance + prices[i] - fee)
        return profit