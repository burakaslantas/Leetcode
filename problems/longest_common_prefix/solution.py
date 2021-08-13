class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            shortest = min(strs, key=len)
            
            for index, char in enumerate(shortest):
                for other in strs:
                    if other[index] != char:
                        return shortest[:index]
            return shortest