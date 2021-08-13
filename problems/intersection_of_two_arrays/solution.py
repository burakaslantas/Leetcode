class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Solution #1
        res = []
        for item in nums1:
            if((item in nums2) and (item not in res)):
                res.append(item)
        return res
        """
        
        Solution #2
        return list(set(nums1) & set(nums2))