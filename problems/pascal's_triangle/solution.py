class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Solution #1
        res = [[1], [1,1]]
        
        if(numRows == 1):
            return [[1]]
        elif(numRows == 2):
            return res
        
        while(numRows-2 > 0):
            temp = []
            for i in range( 1, len(res[-1]) ):
                num1 = res[-1][i-1]
                num2 = res[-1][i]
                temp.append(num1 + num2)
            res += [[1] + temp + [1]]
            numRows -= 1
        
        return res
        """
        
        #Solution #2
        res = [[1]]
        
        while(numRows > 1):
            temp = map(lambda num1, num2: num1 + num2 , [0] + res[-1], res[-1] + [0])
            res += [list(temp)]
            numRows -= 1
            
        return res