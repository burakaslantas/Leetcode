class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first, length):
            if(first == length):
                res.append(nums[:])
            for i in range(first, length):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1, length)
                nums[first], nums[i] = nums[i], nums[first]
            
        length = len(nums)
        res = []
        backtrack(0, length)
        return res
    #Note to myself: Learn DFS Algorithm, Backtracking, difference between "nums[:]"" and "nums"!