class Solution:
    def reverseBits(self, n: int) -> int:
        res, shift = 0, 31
        while(n):
            LeastSignificantBit = (n & 1)
            res += (LeastSignificantBit << shift)
            shift -= 1
            n >>= 1
        return res
        #Note to myself: Learn other solutions.