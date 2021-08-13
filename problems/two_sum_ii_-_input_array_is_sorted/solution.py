class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dictionary
        """seen = {}
        for index, current in enumerate(numbers, 1):
            remaining = target - current
            if(remaining in seen):
                return [seen[remaining], index]
            else:
                seen[current] = index"""
        
        # two-pointer
        """r = len(numbers)-1
        l = 0
        while(l < r):
            if (numbers[r] + numbers[l] > target):
                r -= 1
            elif (numbers[r] + numbers[l] < target):
                l += 1
            else:
                return [l+1, r+1]"""
            
        #binary search
        for index, current in enumerate(numbers):
            remaining = target - current
            
            l = index+1
            r = len(numbers)-1
            while(l <= r):
                mid = (l + r) // 2
                if(remaining > numbers[mid]):
                    l = mid+1
                elif(remaining < numbers[mid]):
                    r = mid-1
                elif(remaining == numbers[mid]):
                    return [index+1, mid+1]
