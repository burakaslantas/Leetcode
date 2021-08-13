class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        """
        Solution #1
        
        dicT = {}
        dicS = {}
        for i in t:
            if(i not in dicT.keys()):
                dicT[i] = 1
            else:
                dicT[i] += 1
        for i in s:
            if(i not in dicS.keys()):
                dicS[i] = 1
            else:
                dicS[i] += 1
        
        for i in t:
            if(i not in dicS.keys()):
                return False
            elif(dicT[i] != dicS[i]):
                return False
            elif(dicT.keys() != dicS.keys()):
                return False
        return True"""
        
        """
        Solution #2
        
        dic = {}
        for i in s:
            if(i not in dic):
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if(i not in dic):
                return False
            else:
                dic[i] -= 1
        
        for i in dic.values():
            if(i != 0):
                return False
        return True"""
        
        #Solution #3
        dic = [0]*26
        for i in s:
            dic[ord(i) - ord('a')] += 1
        for i in t:
            dic[ord(i) - ord('a')] -= 1
        
        for i in range(26):
            if(dic[i] != 0):
                return False
        return True