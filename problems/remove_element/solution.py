class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """leng = len(nums)
        while(leng != 0):
            if val in nums:
                nums.remove(val)
            else:
                break
            leng -= 1"""
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)