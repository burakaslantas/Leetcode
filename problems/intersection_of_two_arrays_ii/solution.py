class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Solution #1
        res = []
        for num1 in nums1:
            if(num1 in nums2):
                res.append(num1)
                nums2.remove(num1)
        return res
        """
        
        """
        Solution #2
        hashMap = {}
        res = []
        
        if( len(nums1) < len(nums2) ):
            array1, array2 = nums1, nums2
        else:
            array1, array2 = nums2, nums1
        
        for num in array1:
            if(num not in hashMap):
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        for num in array2:
            if(num in hashMap and hashMap[num] > 0):
                res.append(num)
                hashMap[num] -= 1
        
        return res
        """
        
        #Solution #3
        nums1.sort()
        nums2.sort()
        i = j = k = 0
        
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] > nums2[j]):
                j += 1
            elif(nums1[i] < nums2[j]):
                i += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
                
        return nums1[:k]