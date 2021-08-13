class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i in range(len(s)):
            if(s[i] not in dic.keys()):
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for index, value in enumerate(s):
            if (dic[value] == 1):
                return index
        return -1