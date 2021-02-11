class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buffer = {}
        for i in range(len(nums)):
            if nums[i] in buffer:
                return [buffer[nums[i]], i]
            else:
                buffer[target - nums[i]] = i