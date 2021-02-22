class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """total = 0
        res = []
        for i in range(len(nums)):
            if i == 0:
                total += nums[0]
                res.append(total)
            else:
                total += nums[i]
                res.append(total)
        return res"""
        
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1
        return nums