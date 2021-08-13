class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Solution #1
        res = ""
        for char in address:
            if(char == "."):
                res += "[.]"
            else:
                res += char
        return res
        """
        
        #Solution #2
        return '[.]'.join(address.split("."))