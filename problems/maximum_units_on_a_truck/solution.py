class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse = True, key = lambda x: x[1])
        res = 0
        for item in boxTypes:
            if(truckSize >= item[0]):
                truckSize -= item[0]
                res += item[0] * item[1]
            else:
                res += item[1] * truckSize
                break
        return res