class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(first, length):
            if(first == length):
                if(nums[:] not in output):
                    output.append(nums[:])
            for i in range(first, length):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1, length)
                nums[first], nums[i] = nums[i], nums[first]
        length = len(nums)
        backtrack(0, length)
        return output