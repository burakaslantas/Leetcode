class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Solution #1
        def helper(s, l, r):
            while(l < r):
                if(s[l] != s[r]):
                    return False
                l += 1
                r -= 1
            return True
            
        l = 0
        r = len(s) - 1
        while(l < r):
            if(s[l] != s[r]):
                return helper(s, l+1, r) or helper(s, l, r-1)
            l += 1
            r -= 1
        return True
        """
    
        """
        Solution #2
        l = 0
        r = len(s) - 1
        
        while(l < r):
            if(s[l] != s[r]):
                leftRemoved = s[l+1 : r+1]
                rightRemoved = s[l : r]
                return (leftRemoved == leftRemoved[::-1]) or (rightRemoved == rightRemoved[::-1])
            l += 1
            r -= 1
        return True
        """
        
        #Solution #3
        #Using Recursion
        def valid(string, start, end, d): # d: num of chars you can delete at most
            if(start >= end):
                return True
            if(string[start] == string[end]):
                return valid(string, start+1, end-1, d)
            else:
                return d > 0 and (valid(string, start+1, end, d-1) or valid(string, start, end-1, d-1))
            
        return valid(s, 0, len(s)-1, 1)
        
        