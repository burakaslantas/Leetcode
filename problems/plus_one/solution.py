class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Solution #1
        for i in range(len(digits)-1, -1, -1):
            if(i == len(digits)-1):
                carry = (digits[-1] + 1) // 10
                digits[-1] = (digits[-1] + 1) % 10
            else:
                original_digit = digits[i]
                digits[i] = (digits[i] + carry) % 10
                carry = (original_digit + carry) // 10
        if(carry):
            digits.insert(0, carry)
        return digits
        """
        
        #Solution #2
        for i in range(len(digits)-1, -1, -1):
            if(digits[i] == 9):
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits