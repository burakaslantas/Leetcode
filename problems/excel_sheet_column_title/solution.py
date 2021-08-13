class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while(columnNumber > 0):
            columnNumber -= 1 #To across from excel index system to char index system. 
            digit = columnNumber % 26
            res.append( chr(ord('A') + digit) )
            columnNumber = columnNumber // 26
        return "".join(item for item in res[::-1])