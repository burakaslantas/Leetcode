class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buyPrice = 100000
        for i in range(len(prices)):
            if(prices[i] < buyPrice):
                buyPrice = prices[i]
            elif(prices[i] > buyPrice):
                profit = max(profit, prices[i]-buyPrice)
        return profit