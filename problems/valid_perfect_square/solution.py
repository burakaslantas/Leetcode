class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """r = num
        while (r*r > num):
            r = (r + (num//r)) // 2
        return r*r == num"""
        
        """i = 1
        while (num > 0):
            num -= i
            i += 2
        return num == 0"""
        
        left = 0
        right = num
        
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (mid*mid == num):
                return True
            elif (mid*mid > num):
                right = mid - 1
            else:
                left = mid + 1
        return False