class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Solution #1
        res = []
        i = 0
        while(i < n):
            res += [nums[i], nums[i+n]]
            i += 1
        return res
        """
        
        #Solution #2
        for i in range(n):
            nums[i+n] |= nums[i] << 10 # nums[i+n] = nums[i] + nums[i+n]
        
        for j in range(n):
            nums[2 * j] = (nums[j+n] & 0xFFC00) >> 10 # AND 1111 1111 1100 0000 0000 => 0xFFC00
            nums[2 * j + 1] = nums[j+n] & 0x003FF  #AND 0000 0000 0011 1111 1111 => 0x003FF
        
        return nums