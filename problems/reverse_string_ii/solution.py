class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        pointer = 0
        end = len(s)
        s = list(s)

        while(pointer < end):
            s[pointer : pointer+k] = reversed(s[pointer : pointer+k])
            pointer += 2*k
        return ''.join(item for item in s)