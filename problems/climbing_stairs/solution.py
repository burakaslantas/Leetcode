class Solution:
    def climbStairs(self, n: int) -> int:
        """
        def Factorial(n):
            if (n == 0):
                return 1
            else:
                return n * Factorial(n-1)
            
        two_num = n//2
        result = 0
        for i in range(two_num+1):
            twos = i
            ones = n - twos*2
            result += (Factorial(ones+twos)//(Factorial(ones) * Factorial(twos)))
        return result
        """
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a
    
    