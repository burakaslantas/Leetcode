class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = []
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1
        
        while( pointer1 >= 0 or pointer2 >= 0 ):
            #check num1 whether if used entirely or used partially
            if( pointer1 >= 0 ):
                digit1 = ord( num1[ pointer1 ] ) - ord('0')
            else:
                digit1 = 0
            #check num2 whether if used entirely or used partially
            if( pointer2 >= 0 ):
                digit2 = ord( num2[ pointer2 ] ) - ord('0')
            else:
                digit2 = 0
            
            resDigit = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10
            res.append(resDigit)
            pointer1 -= 1
            pointer2 -= 1
            
            
        if(carry):
            res.append(carry)
        
        return ''.join( str(digit) for digit in res[::-1] )