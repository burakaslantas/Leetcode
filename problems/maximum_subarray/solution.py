class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #iterate through nums
        #look current item, add them to current total
        #if total is positive, continue adding items
        #else total is negative, reset it to 0 before passing the other item
        #take maximum of total on max_total variable
        #return max_total
        maxTotal = nums[0]
        total = nums[0]
        for item in nums[1:]:
            total = max(item, total + item)
            maxTotal = max(maxTotal, total)
        return maxTotal