class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Brute Force (Not Valid Solution)
        primes = 0
        
        if(n < 3):
            return 0
        
        for isprime in range(2, n):
            for factor in range(2, ( isprime ** (1/2) )):
                if(isprime % factor == 0):
                    break
            #why "else" is outside of for loop?
            else:
                primes += 1
        
        return primes
        """
        
        """
        #Solution #1
        if(n <= 2):
            return 0
        
        markedNotPrime = {}
        for isprime in range(2, int(sqrt(n)) + 1):
            if(isprime not in markedNotPrime):
                for num in range(isprime*isprime, n, isprime):
                    markedNotPrime[num] = -1
        
        return n - len(markedNotPrime) - 2
        """
    
        #Solution #2
        if(n <= 2):
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        
        for isprime in range(2, int(sqrt(n)) + 1):
            if(primes[isprime]):
                for num in range(isprime*isprime, n, isprime):
                    primes[num] = False
        
        return sum(primes)