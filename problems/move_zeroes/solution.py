class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        length = len(nums) 
        while(i < length):
            if(nums[i] == 0):
                del nums[i]
                length -= 1
                count += 1
            else:
                i += 1
            
        while(count > 0):
            nums.append(0)
            count -= 1
        
        
        
        """snowball = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                snowball += 1
            else:
                temp, nums[i] = nums[i], 0
                nums[i-snowball] = temp"""
                