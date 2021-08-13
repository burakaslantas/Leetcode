class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s) - 1):
            if romans[s[i]] >= romans[s[i+1]]:
                res += romans[s[i]]
            else:
                res -= romans[s[i]]
        res += romans[s[-1]]
        return res