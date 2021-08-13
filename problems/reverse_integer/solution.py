class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        else:
            sign = -1
        mutlak = abs(x)
        reversedx = sign * int(str(mutlak)[::-1])
        return reversedx if (-2)**31 < reversedx < 2**31 else 0