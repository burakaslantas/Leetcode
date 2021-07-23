class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pointerA = len(a) - 1
        pointerB = len(b) - 1
        carry = 0
        res = []
        while(pointerA > -1 or pointerB > -1):
            if(pointerA < 0):
                digitA = 0
            else:
                digitA = ord(a[pointerA]) - ord('0')
            if(pointerB < 0):
                digitB = 0
            else:
                digitB = ord(b[pointerB]) - ord('0')
                
            total = digitA + digitB + carry
            res.append(total % 2)
            carry = total // 2
            pointerA -= 1
            pointerB -= 1
        if(carry):
            res.append(carry)
        
        return ''.join(str(digit) for digit in res[::-1])