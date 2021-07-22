class Solution:
    def validPalindrome(self, s: str) -> bool:
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