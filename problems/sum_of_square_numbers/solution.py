class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        Solution #1
        upTo = int(sqrt(c)) + 1
        
        for a in range(upTo):
            for b in range(upTo):
                if(a == sqrt( c - b ** 2 )):
                    return True
        return False
        """
        
        #Solution #2
        upTo = int(sqrt(c)) + 1
        
        for b in range(upTo):
            a = sqrt( c - b ** 2 )
            if(a == int(a)):
                return True
        return False