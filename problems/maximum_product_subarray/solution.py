class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # assign nums[0] to "result", "min product", and "max product"
        # iterate over nums, keep current number
        # also keep both "max product" and "min product"
        # max product = maximum of "current number", "max product * current number", "min product * current number"
        # min product = minimum of "current number", "max product * current number", "min product * current number"
        # before jumping to next element over the nums, keep maximum of max product in the result
        # after the iteration was finished, return the result
        
        result = maximumProduct = minimumProduct = nums[0]
        
        for currentNum in nums[1:]:
            temp = max(currentNum, maximumProduct * currentNum, minimumProduct * currentNum)
            minimumProduct = min(currentNum, maximumProduct * currentNum, minimumProduct * currentNum)
            maximumProduct = temp
            result = max(result, maximumProduct)
        return result
