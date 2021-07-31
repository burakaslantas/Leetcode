class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Solution #1
        res = [nums[0]]
        for item in nums[1:]:
            res.append( res[-1] + item )
        return res
        """
    
        #Solution #2
        for item in range(1, len(nums)):
            nums[item] += nums[item-1]
        return nums