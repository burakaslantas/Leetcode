class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1], [1,1]]
        
        if(rowIndex == 0):
            return res[0]
        elif(rowIndex == 1):
            return res[-1]
        
        while(rowIndex > 1):
            temp = []
            for i in range( 1, len(res[-1]) ):
                num1 = res[-1][i-1]
                num2 = res[-1][i]
                temp.append(num1 + num2)
            res += [[1] + temp + [1]]
            rowIndex -= 1
        
        return res[-1]