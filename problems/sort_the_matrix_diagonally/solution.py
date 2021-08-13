class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Solution #1
        rowLength = len(mat)
        columnLength = len(mat[0])
        diagonals = defaultdict(list)
        
        for row in range(rowLength):
            for column in range(columnLength):
                diagonals[row - column].append(mat[row][column])
                
        for diagonal in diagonals.items():
            heapq.heapify(diagonal[1])
            #diagonal[1].sort() *This is doing the same thing with the above code
            
        for row in range(rowLength):
            for column in range(columnLength):
                value = heapq.heappop(diagonals[row - column])
                #value = diagonals[row - column].pop(0) *This is doing the same thing with the above code
                mat[row][column] = value
        
        return mat
        """
        
        
        #Solution #2
        rowLength = len(mat)
        columnLength = len(mat[0])
        diagonals = defaultdict(list)
        
        def sortDiagonal(row, column):
            diagonal = []
            diagonalLength = min(rowLength - row, columnLength - column)
            
            for i in range(diagonalLength):
                diagonal.append(mat[row+i][column+i])
            
            heapq.heapify(diagonal)
            #diagonal.sort() *This is doing the same thing with the above code
            
            for i in range(diagonalLength):
                mat[row+i][column+i] = heapq.heappop(diagonal) #diagonal.pop(0)
                #mat[row+i][column+i] = diagonal.pop(0) *This is doing the same thing with the above code
        
        for row in range(rowLength):
            sortDiagonal(row, 0)
            
        for column in range(columnLength):
            sortDiagonal(0, column)
            
        return mat
        
        
        #Note to myself: Learn Approach 3, counting sort, Defaultdict in Python and heaps!