class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Solution #1
        leftSum, rightSum = 0, sum(nums)
        for i in range(len(nums)):
            rightSum -= nums[i]
            if(leftSum == rightSum):
                return i
            leftSum += nums[i]
        return -1
        """
        
        #Solution #2
        total = sum(nums)
        leftsum = 0
        for i, curr in enumerate(nums):
            if leftsum == (total - leftsum - curr):
                return i
            leftsum += curr
        return -1