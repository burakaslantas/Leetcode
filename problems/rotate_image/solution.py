class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        #Solution #1
        #first transpose (on diagonal from top-left to bottom-right) the matrix
        n = len(matrix)
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        #second reflect the matrix
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - 1 - col] = matrix[row][n - 1 - col], matrix[row][col]
        """
        
        #Solution #2
        #first transpose (on diagonal from bottom-left to top-right) the matrix
        n = len(matrix)
        for row in range(n):
            for col in range(n - 1 - row, -1, -1):
                matrix[row][col], matrix[n - 1 - col][n - 1 - row] = matrix[n - 1 - col][n - 1 - row], matrix[row][col]
                
        #second reflect matrix top-bottom
        matrix.reverse()

