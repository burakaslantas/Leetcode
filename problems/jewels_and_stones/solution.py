class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = {item:1 for item in jewels}
        res = 0
        for item in stones:
            if(item in hashmap):
                res += 1
        return res