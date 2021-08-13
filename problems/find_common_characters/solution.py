class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = list(words[0])
        for word2 in words[1:]:
            temp = []
            for letter in word2:
                if (letter in res):
                    temp.append(letter)
                    res.remove(letter)
            res = temp
        return res