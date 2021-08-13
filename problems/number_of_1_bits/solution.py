class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Solution #1
        res = 0
        for i in range(32):
            LeastSignificantBit = n % 2
            if(LeastSignificantBit == 1):
                res += 1
            n = n >> 1
        return res
        """
        
        #Solution #2
        res = 0
        while(n != 0):
            res += 1
            n &= (n - 1)
        return res