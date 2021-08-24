class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        Solution #1
        stack = []
        for i in range(len(heights)):
            while( len(stack) and heights[i] >= heights[stack[-1]] ):
                stack.pop(-1)
            if( len(stack) == 0 or heights[i] < heights[stack[-1]] ):
                stack.append(i)
        return stack
        """
        
        #Solution #2
        stack = [len(heights)-1]
        for i in range(len(heights)-2, -1, -1):
            if(heights[i] > heights[stack[-1]]):
                stack.append(i)
        stack.reverse()
        return stack
            
