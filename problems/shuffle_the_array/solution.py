class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for first, second in zip(nums[:n], nums[n:]):
            res += [first, second]
        return res