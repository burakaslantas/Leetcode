class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """w1 = ""
        w2 = ""
        lstlen = max(len(word1), len(word2))
        for char in word1:
            w1 += char
        for char in word2:
            w2 += char
        return w1 == w2"""
        
        return ''.join(word1) == ''.join(word2)