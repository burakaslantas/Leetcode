class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """wealth = 0
        sum = 0
        for customer in accounts:
            for bank in customer:
                sum += bank
            if sum > wealth:
                wealth = sum
            sum = 0
        return wealth"""
        
        return max(sum(customer) for customer in accounts)