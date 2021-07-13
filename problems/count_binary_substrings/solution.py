class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        consecutiveCounter = 1
        temp = []
        for i in range(1, len(s)):
            if(s[i] == s[i-1]):
                consecutiveCounter += 1
            else:
                temp += [consecutiveCounter]
                consecutiveCounter = 1
        temp += [consecutiveCounter]
        
        for i in range(1, len(temp)):
            res += min(temp[i-1], temp[i])
        return res