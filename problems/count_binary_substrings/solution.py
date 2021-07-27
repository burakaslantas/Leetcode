class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Solution #1
        res = 0
        sameTypes = []
        consecutiveCounter = 1
        for i in range(1, len(s)):
            if( s[i] != s[i-1] ):
                sameTypes.append(consecutiveCounter)
                consecutiveCounter = 1
            else:
                consecutiveCounter += 1
        sameTypes.append(consecutiveCounter)
        
        for j in range(1, len(sameTypes)):
            res += min( sameTypes[j-1], sameTypes[j] )
        
        return res
        """
        
        #Solution #2
        answer, prev, curr = 0, 0, 1
        #prev = preview consecutive counter
        #curr = current consecutive counter
        
        for i in range(1, len(s)):
            if( s[i-1] != s[i] ):
                answer += min( prev, curr )
                prev, curr = curr, 1
            else:
                curr += 1
        return answer + min( prev, curr )
        