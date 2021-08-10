class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Solution #1
        res = -math.inf
        for start in range(len(nums)):
            currentSubArray = 0
            for index in range(start, len(nums)):
                currentSubArray += nums[index]
                res = max(res, currentSubArray)
        return res
        """
        
        """
        Solution #2
        
        #iterate through nums
        #look current item, add them to currentTotal
        #if currentTotal is positive, continue adding items
        #else currentTotal is negative, reset it to 0 before passing the other item
        #take maximum of currentTotal on max_total variable
        #return max_total
        
        maxTotal = currentTotal = nums[0]
        for item in nums[1:]:
            currentTotal = max(item, currentTotal + item)
            maxTotal = max(maxTotal, currentTotal)
        return maxTotal
        """
        
        #Solution #3
        def helper(nums, left, right):
            if(left > right):
                return -math.inf
            
            current = maxLeftSum = maxRightSum = 0
            mid = left + (right-left) // 2
            
            #check left side
            for i in range(mid-1, left-1, -1):
                current += nums[i]
                maxLeftSum = max(maxLeftSum, current)
            current = 0
            #check right side
            for i in range(mid+1, right+1):
                current += nums[i]
                maxRightSum = max(maxRightSum, current)
            
            entireArrayMaxSum = maxLeftSum + nums[mid] + maxRightSum
            
            #look only left side
            onlyLeftMaxSum = helper(nums, left, mid-1)
            #look only right side
            onlyRightMaxSum = helper(nums, mid+1, right)
            
            return max(onlyLeftMaxSum, entireArrayMaxSum, onlyRightMaxSum)
            
        return helper(nums, 0, len(nums)-1)
        
        