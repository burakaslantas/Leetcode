class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        #Solution #1 (Brute Force)
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
        
        """
        #Solution #2
        m = len(num1); n = len(num2)
        position = [0 for _ in range(m + n)]
        
        for i in range(m-1, -1 , -1):
            digit1 = num1[i]
            digit1 = ord(digit1) - ord('0')
            for j in range(n-1 , -1, -1):
                
                digit2 = num2[j]
                digit2 = ord(digit2) - ord('0')
                p1 = i + j; p2 = i + j + 1
                product = digit1 * digit2 + position[p2]
                position[p1] += product // 10
                position[p2] = product % 10
        
        indLeadingZero = 0
        while(indLeadingZero < len(position)-1 and position[indLeadingZero] == 0):
            indLeadingZero += 1
        
        return "".join(str(x) for x in position[indLeadingZero : ])
        """
        
        #Solution #3
        power = 1
        intNum1 = intNum2 = 0
        for digit1 in num1[::-1]:
            intNum1 += power * (ord(digit1) - ord('0'))
            power *= 10
        power = 1
        for digit2 in num2[::-1]:
            intNum2 += power * (ord(digit2) - ord('0'))
            power *= 10
        
        #Using Russian peasant multiplication
        res = 0
        while(intNum1 != 0):
            if(intNum1 & 1): #This is the same thing with "intNum1 % 2 != 0"
                res += intNum2
            
            intNum1 >>= 1 #This is the same thing with "intNum1 //= 2"
            intNum2 <<= 1 #This is the same thing with "intNum2 *= 2"
            
        return str(res)