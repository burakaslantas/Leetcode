class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #choose first element
        results = []
        for i in range(len(nums)):
            firstelement = nums[i]
            for j in range(len(nums)):
                if (i != j):
                    secondelement = nums[j]
                    if (firstelement + secondelement == target):
                        results.append(i)
                        results.append(j)
                        return results
        #use for loop start index 0 to index -1
        #use another loop start index 0 to index -1
        #but if i == j pass that index in another loop