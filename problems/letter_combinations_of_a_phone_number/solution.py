class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2 : ['a', 'b', 'c'],
               3 : ['d', 'e', 'f'],
               4 : ['g', 'h', 'i'],
               5 : ['j', 'k', 'l'],
               6 : ['m', 'n', 'o'],
               7 : ['p', 'q', 'r', 's'],
               8 : ['t', 'u', 'v'],
               9 : ['w', 'x', 'y', 'z']}
        powerList = []
        for i in range(len(digits)):
            num = int(digits[i])
            powerList.append(dic[num])
        print("powerList =>", powerList)
        res = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return dic[int(digits)]
        
        for i in range(len(powerList)-1):
            if (len(res) == 0):
                res = powerList[i]
            current = powerList[i+1]
            print(res)
            print(current)
            temp = []
            for i in res:
                for j in current:
                    temp.append(i + j)
            res = temp
        return res