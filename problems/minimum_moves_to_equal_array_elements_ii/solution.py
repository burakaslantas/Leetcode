class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        mid = (left + right) // 2
        res = 0
        for item in nums:
            res += abs(item - nums[mid])
        return res
        #Note to myself = Learn other solutions.