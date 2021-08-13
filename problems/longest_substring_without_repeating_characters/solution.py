class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Solution #1
        curr = ""
        res = 0
        for left_pointer in range(len(s)):
            for right_pointer in range(left_pointer, len(s)):
                if(s[right_pointer] in curr):
                    res = max(res, len(curr))
                    curr = ""
                    break
                else:
                    curr += s[right_pointer]
        res = max(res, len(curr))
        return res
        """
        
        #Solution #2
        seen = {}
        n = len(s)
        close_window_pointer = 0
        open_window_pointer = 0
        ans = 0
        
        while( open_window_pointer < n ):
            if( s[open_window_pointer] in seen ):
                close_window_pointer = max(seen[ s[open_window_pointer] ] + 1, close_window_pointer)
            ans = max(ans, open_window_pointer - close_window_pointer + 1)
            seen[ s[open_window_pointer] ] = open_window_pointer
            open_window_pointer += 1
        return ans
        
        #Note to myself: Learn other solutions (Approach 3: Sliding Window Optimized). 
        