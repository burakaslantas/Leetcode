class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        maxValue = 0
        maxKey = ""
        for key in dic.keys():
            if dic[key] > maxValue:
                maxValue = dic[key]
                maxKey = key
                if maxValue > (len(nums)/2):
                    break
        return maxKey"""
        
        """nums.sort()
        return nums[len(nums)//2]"""
        
        candidate, count = nums[0], 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                candidate, count = num, 1
            else:
                count -= 1
        return candidate