class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for item in s:
            if(len(stack) == 0 or item != stack[-1]):
                stack.append(item)
            elif(item == stack[-1]):
                stack.pop(-1)
        return ''.join(stack)