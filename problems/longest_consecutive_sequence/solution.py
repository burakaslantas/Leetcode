class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        #Solution #1 (Brute Force)
        maxCount = 0
        
        for num in nums:
            currNum = num
            currCount = 1
            
            while(currNum + 1 in nums):
                currNum += 1
                currCount += 1
                
            maxCount = max(maxCount, currCount)
            
        return maxCount
        """
    
        """
        #Solution #2
        if(len(nums) == 0):
            return 0
        
        nums.sort()
        maxCount = currCount = 1
        
        for i in range(1, len(nums)):
            if(nums[i-1] != nums[i]):
                if(nums[i-1] + 1 == nums[i]):
                    currCount += 1
                else:
                    maxCount = max(maxCount, currCount)
                    currCount = 1
                    
        return max(maxCount, currCount)
        """
        
        #Solution #3
        numsSet = set(nums)
        maxCount = 0
        
        for num in numsSet:
            #Find the start number of streak
            if(num - 1 not in numsSet):
                currNum = num
                currCount = 1
            
                while(currNum + 1 in numsSet):
                    currNum += 1
                    currCount += 1
                
                maxCount = max(maxCount, currCount)
            
        return maxCount
