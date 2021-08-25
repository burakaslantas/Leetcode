class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            sameRow = {}
            sameCol = {}
            
            for col in range(9):
                if(board[col][row] in sameCol):
                    return False
                if(board[row][col] in sameRow):
                    return False
                if(board[row][col] != '.'):
                    sameRow[ board[row][col] ] = 1
                if(board[col][row] != '.'):
                    sameCol[ board[col][row] ] = 1
                
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                same3x3 = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3) if board[row][col] != '.']
                if( len(same3x3) != len( set(same3x3) ) ):
                    return False
        return True