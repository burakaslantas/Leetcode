class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Solution #1
        
        dic = {}
        for i in range(len(nums)):
            if(nums[i] not in dic):
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        
        for key in dic:
            if(dic[key] == 1):
                return key
        """
        
        """
        Solution #2
        
        return 2 * sum(set(nums)) - sum(nums)
        """
        
        #Solution #3
        
        x = 0
        for i in nums:
            x ^= i
        return x