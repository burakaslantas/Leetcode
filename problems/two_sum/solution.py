class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, current in enumerate(nums):
            remaining = target - current
            
            if (remaining in seen):
                return [index, seen[remaining]]
            else:
                seen[current] = index