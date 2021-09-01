class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Note: This is a dynamic programming[1] question. Usually, solving and fully understanding a dynamic programming problem is a 4 step process:
        #     * Start with the recursive backtracking solution
        #     * Optimize by using a memoization table (top-down[2] dynamic programming)
        #     * Remove the need for recursion (bottom-up dynamic programming)
        #     * Apply final tricks to reduce the time / memory complexity
        
        """
        #NOT FINISHED CODE!
        #1 - iterate over nums, starting from 0th index
        #2 - look current possible jumps and take the maximum number, those are in the nums[currentIndex + 1 : currentIndex + currentNumber + 1]
        #3 - do the 2nd step until "reach the end of the nums", and return true
        #4 Otherwise, if "before index == current index", return false
        
        
        
        # bInd => before index
        # cInd => current index
        # n => length of nums
        def takeMaximumNum(nums, start, end):
            maxNum = -1
            maxInd = -1
            for i in range(start, end):
                if(start >= len(nums)):
                    break
                if(maxNum < nums[i]):
                    maxNum = nums[i]
                    maxInd = i
            return [maxInd, maxNum]
        
        #print( takeMaximumNum(nums, 1, 3) )
        
        n = len(nums)
        currentInd = beforeInd = 0
        while(currentInd < n):
            currentNumber = nums[currentInd]
            
            if(currentInd + 1 < n):
                maxNumPair = takeMaximumNum(nums, currentInd + 1, currentInd + currentNumber + 1)
            
            beforeInd = currentInd
            currentInd = maxNumPair[0]
            currentNumber = maxNumPair[1]
            
            print("Before =>", beforeInd)
            print("Current =>", currentInd)
            if(beforeInd == currentInd):
                return False
        return True
        """
        
        
        #Solution #1
        lastPosition = len(nums) - 1
        for i in range( len(nums) - 1, -1, -1 ):
            if( i + nums[i] >= lastPosition ):
                lastPosition = i
        return lastPosition == 0
