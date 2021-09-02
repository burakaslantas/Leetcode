class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Example #1
        # [1, 2, 3],
        # [4, 5, 6],
        # [7, 8, 9]
        
        # Example #2
        # [1,  2,  3,  4],
        # [5,  6,  7,  8],
        # [9, 10, 11, 12]
        
        result = []
        lenRow, lenCol = len(matrix), len(matrix[0])
        top = left = 0
        bottom, right = lenRow - 1, lenCol - 1
        
        while(len(result) < lenRow * lenCol):
            #Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            
            #Traverse from top to bottom
            for row in range(top + 1, bottom + 1):
                result.append(matrix[row][right])
            
            if(top != bottom):
                #Traverse from right to left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][col])
                
            if(left != right):
                #Traverse from bottom to top
                for row in range(bottom - 1, top, -1):
                    result.append(matrix[row][left])
            
            left += 1
            top += 1
            right -= 1
            bottom -= 1
        
        return result
        
        """
        This code doesn't work.
        res = []
        startRow = 0
        endRow = len(matrix)
        startCol = 0
        endCol = len(matrix[0])
        
        while( startRow < endRow or startCol < endCol ):
            #move right => row constant, column increasing
            for i in range(startCol, endCol):
                res.append(matrix[startRow][i])
                startRow += 1
            #move down => row increasing, column constant
            for i in range(startRow, endRow):
                res.append(matrix[i][endCol])
                endCol -= 1
            #move left => row constant, column decreasing
            for i in range(endCol, startCol, -1):
                res.append(matrix[endRow][i])
                endRow -= 1
            #move up => row decreasing, column constant
            for i in range(endRow, startRow, -1):
                res.append(matrix[i][startCol])
                startCol += 1
            
        return res
        """
