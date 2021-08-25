class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        upTo = int(sqrt(c)) + 1
        
        for a in range(upTo):
            for b in range(upTo):
                if(a == sqrt( c - b ** 2 )):
                    return True
        return False
        """
    
        upTo = int(sqrt(c)) + 1
        
        for b in range(upTo):
            a = sqrt( c - b ** 2 )
            if(a == int(a)):
                return True
        return False