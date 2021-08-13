class Solution:
    def countBits(self, num: int) -> List[int]:
        """results = []
        for i in range(num+1):
            onesNum = bin(i)[2:]
            res = 0
            for digit in onesNum:
                print(digit)
                if int(digit) == 1:
                    res += 1
            results.append(res)
        return results"""
        
        res = [0]
        while (len(res) <= num):
            res.extend([i+1 for i in res])
        return res[:num+1]