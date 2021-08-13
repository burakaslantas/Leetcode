class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Solution #1
        i, missing_number_counter, res, length = 0, 0, 1, len(arr)
        
        while(i < length):
            if(arr[i] != res):
                missing_number_counter += 1
                if(missing_number_counter == k):
                    return res
            elif(arr[i] == res):
                i += 1
            res += 1
            
        return arr[-1] + (k - missing_number_counter)
        """
        
        """
        Solution #2
        if(k < arr[0]):
            return k
        else:
            k -= (arr[0] - 1)
            
        for i in range(1, len(arr)):
            currentMissing = arr[i] - arr[i-1] - 1
            if(k <= currentMissing):
                return arr[i-1] + k
            else:
                k -= currentMissing
                
        return arr[-1] + k
        """
        
        #Solution #3
        left, right = 0, len(arr) - 1
        
        while(left <= right):
            pivot = left + (right-left) // 2
            currentMissing = arr[pivot] - (pivot + 1)
            if(currentMissing < k):
                left = pivot + 1
            else:
                right = pivot - 1
        
        #left = right + 1
        #currentMissing = arr[right] - right - 1
        #arr[right] + k - (arr[right] - right - 1) = left + k
        return left + k