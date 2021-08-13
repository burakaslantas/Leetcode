class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(item[::-1] for item in s.split(' '))