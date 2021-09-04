class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Note to myself: Solve this question later again.
        
        #This is NOT my solution.
        '''
        :type coins: list of int
        :type amount: int
        :rtype: int
        '''

        # This table will store the answer to our sub problems
        dp = [amount + 1] * (amount + 1)

        '''
        The answer to making change with minimum coins for 0
        will always be 0 coins no matter what the coins we are
        given are
        '''
        dp[0] = 0

        # Solve every subproblem from 1 to amount
        for i in range(1, amount + 1):
            # For each coin we are given
            for j in range(0, len(coins)):
                # If it is less than or equal to the sub problem amount
                if coins[j] <= i:
                    # Try it. See if it gives us a more optimal solution
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)

        '''
        dp[amount] has our answer. If we do not have an answer then dp[amount]
        will be amount + 1 and hence dp[amount] > amount will be true. We then
        return -1.
  
        Otherwise, dp[amount] holds the answer
        '''

        return -1 if dp[amount] > amount else dp[amount]
        
        
        """
        NOT FINISHED CODE
        if(amount == 0):
            return 0
        
        n = len(coins)
        res = []
        count = 0
        def helper(coins, amount):
            count = 0
            if(count == amount):
                return 0
            while(count < amount):
                for i in range(n):
                    total = 1 + helper(coins, amount)
                    res.append(total)
                count += 1
            return res
        
        return helper(coins, amount)
        """
        
