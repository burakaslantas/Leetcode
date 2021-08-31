class Solution:
    def numDecodings(self, s: str) -> int:
        """
        #Solution #1
        @lru_cache(maxsize=None)
        def helper(index, s):
            if(index == len(s)):
                return 1
            #check for one digit
            if(s[index] == "0"):
                return 0
            if(index == len(s)-1):
                return 1
            answer = helper(index+1, s)
            
            #check for double digit
            if(int(s[index] + s[index + 1]) <= 26):
                answer += helper(index+2, s)
            
            return answer
        return helper(0, s)
        """
        
        #Solution #2
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        
        if(s[0] == "0"):
            dp[1] = 0
        else:
            dp[1] = 1
        
        for i in range(2, len(dp)):
            #check for one digit
            if(s[i-1] != "0"):
                dp[i] = dp[i - 1]
            #check for double digit
            twoDigit = int(s[i - 2 : i])
            if(twoDigit >= 10 and twoDigit <= 26):
                dp[i] += dp[i - 2]
        return dp[len(s)]
