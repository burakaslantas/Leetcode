class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def robFrom(i, nums):
            if(i >= n):
                return 0
            
            if i in cache:
                return cache[i]
            
            ans = max(nums[i] + robFrom(i+2, nums), robFrom(i+1, nums))
            cache[i] = ans
            
            return ans
        return robFrom(0, nums)
