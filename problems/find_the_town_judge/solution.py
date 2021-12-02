class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if(len(trust) < n - 1):
            return -1
        
        enteringEdges = [0] * (n + 1)
        
        for pair in trust:
            enteringEdges[ pair[0] ] -= 1
            enteringEdges[ pair[1] ] += 1
        
        for i in range(1, n+1):
            if(enteringEdges[i] == n - 1):
                return i
            
        return -1
