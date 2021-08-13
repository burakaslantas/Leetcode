class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        gause = max(candies) - extraCandies
        return [gause <= candy for candy in candies]