class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Solution #1
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    #res.append((i, j))
                    res += 1
        return res
        """
        
        """
        Solution #2
        hashmap_count = {}
        res = 0
        for item in nums:
            if(item not in hashmap_count):
                hashmap_count[item] = 1
            else:
                hashmap_count[item] += 1
        
        for value in hashmap_count.values():
            res += ( value * (value-1) ) // 2
            #Combination of (value, 2)
        return res
        """
        
        #Solution #3
        hashmap = {}
        res = 0
        #Combination of (value, 2) is equal to sum of this array (1, 2, 3, ..... value-1) which is ((value-1) * value) / 2
        for num in nums:
            if(num not in hashmap):
                hashmap[num] = 1
            else:
                res += hashmap[num]
                hashmap[num] += 1
        return res