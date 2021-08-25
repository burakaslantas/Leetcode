class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        #Solution #1
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
        """
        
        #Solution #2
        # "r" stands for "row"
        # "c" stands for "column"
        n = 9
        
        # vvv ..:: Not Works Here ::.. vvv #
        #What are the wrong things here?
        
        #rows = [set()] * n
        #columns = [set()] * n
        #boxes3x3 = [set()] * n
        
        # vvv ..:: Not Works Here ::.. vvv #
        
        
        # vvv ..:: Works Here ::.. vvv #
        #How it's works here?
        #Answer : https://stackoverflow.com/questions/240178/list-of-lists-changes-reflected-across-sublists-unexpectedly
        
        rows = [set() for _ in range(n)]
        columns = [set() for _ in range(n)]
        boxes3x3 = [set() for _ in range(n)]
        
        # ^^^ ..:: Works Here ::.. ^^^ #

        for r in range(n):
            for c in range(n):
                cell = board[r][c]
                
                if(cell == '.'):
                    continue
                
                if(cell in rows[r]):
                    return False
                rows[r].add(cell)
                
                if(cell in columns[c]):
                    return False
                columns[c].add(cell)
                
                boxInd = (r // 3) * 3 + c // 3
                if(cell in boxes3x3[boxInd]):
                    return False
                boxes3x3[boxInd].add(cell)
                
        return True
    
    #Note to Myself: Learn approaches 2 and 3