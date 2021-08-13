class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = {letter:index for index,letter in enumerate(order)}
        
        for word1, word2 in zip(words, words[1:]):
            if(len(word1) > len(word2) and word1[:len(word2)] == word2):
                return False
            for letter1, letter2 in zip(word1, word2):
                if(hashmap[letter1] > hashmap[letter2]):
                    return False
                elif(hashmap[letter1] < hashmap[letter2]):
                    break
        return True