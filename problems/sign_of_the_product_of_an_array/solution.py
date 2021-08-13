class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Solution #1
        minus = 0
        for item in nums:
            if(item == 0):
                return 0
            elif(item < 0):
                minus += 1
        if(minus % 2):
            return -1
        return 1
        """
        
        #Solution #2
        sign = 1
        for item in nums:
            if(item == 0): return 0
            elif(item < 0): sign = -sign
        return sign