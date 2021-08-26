class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Solution #1 (Brute Force)
        res = []
        lastZeros = 0
        for digit1 in num1[::-1]:
            temp = []
            if(lastZeros):
                temp += [0 for _ in range(lastZeros)]
            digit1 = ord(digit1) - ord('0')
            carry = 0
            for digit2 in num2[::-1]:
                digit2 = ord(digit2) - ord('0')
                cal = digit1 * digit2 + carry
                resDigit = cal % 10
                temp.append(resDigit)
                carry = cal // 10
            if(carry):
                temp.append(carry)
            lastZeros += 1
            temp.reverse()
            res.append(temp)
        
        total = 0
        for i in res:
            tempInt = 0
            power = 1
            for j in i[::-1]:
                tempInt += j * power
                power *= 10
            total += tempInt
        return str(total)
        """
        
        #Solution #2
        power = 1
        intNum1 = intNum2 = 0
        #converting str to int for num1
        for digit1 in num1[::-1]:
            intNum1 += power * (ord(digit1) - ord('0'))
            power *= 10
        #converting str to int for num2
        power = 1
        for digit2 in num2[::-1]:
            intNum2 += power * (ord(digit2) - ord('0'))
            power *= 10
        
        #Using Russian Peasant Multiplication
        res = 0
        while(intNum1 != 0):
            if(intNum1 & 1): #This is the same thing with "intNum1 % 2 != 0"
                res += intNum2
            
            intNum1 >>= 1 #This is the same thing with "intNum1 //= 2"
            intNum2 <<= 1 #This is the same thing with "intNum2 *= 2"
            
        return str(res)